# langchain-snowloader

ServiceNow document loaders for LangChain, powered by [snowloader](https://github.com/ronidas39/snowloader).

Covers six core ServiceNow tables — Incidents, Knowledge Base, CMDB, Changes, Problems, and Service Catalog — with production-grade features like retry logic, delta sync, CMDB relationship traversal, and HTML cleaning.

## Installation

```bash
pip install langchain-snowloader
```

## Usage

```python
from snowloader import SnowConnection
from langchain_snowloader import ServiceNowIncidentLoader

conn = SnowConnection(
    instance_url="https://mycompany.service-now.com",
    username="admin",
    password="password",
)

loader = ServiceNowIncidentLoader(connection=conn, query="active=true")
docs = loader.load()  # list[langchain_core.documents.Document]

# Use with any vector store
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
```

## Available Loaders

| Loader | ServiceNow Table | Description |
|--------|-----------------|-------------|
| `ServiceNowIncidentLoader` | `incident` | IT incidents with optional work notes/comments |
| `ServiceNowKBLoader` | `kb_knowledge` | Knowledge Base articles (HTML auto-cleaned) |
| `ServiceNowCMDBLoader` | `cmdb_ci` | Configuration Items with relationship graph traversal |
| `ServiceNowChangeLoader` | `change_request` | Change requests with implementation windows |
| `ServiceNowProblemLoader` | `problem` | Problems with root cause and known error tracking |
| `ServiceNowCatalogLoader` | `sc_cat_item` | Service catalog items |

## CMDB with Relationships

```python
from langchain_snowloader import ServiceNowCMDBLoader

loader = ServiceNowCMDBLoader(
    connection=conn,
    ci_class="cmdb_ci_server",
    include_relationships=True,
)

docs = loader.load()
print(docs[0].page_content)
# Configuration Item: web-prod-01
# Class: cmdb_ci_server
# ...
# Relationships:
#   -> db-prod-01 (Depends on::Used by)
#   <- load-balancer-01 (Depends on::Used by)
```

## Delta Sync

Only fetch records updated since your last sync:

```python
from datetime import datetime, timezone

loader = ServiceNowIncidentLoader(connection=conn)
docs = loader.load()
last_sync = datetime.now(timezone.utc)

# Next run — only get changes
updated = loader.load_since(last_sync)
```

## Lazy Loading

Stream documents one at a time for memory efficiency:

```python
for doc in loader.lazy_load():
    print(f"[{doc.metadata['number']}] {doc.page_content[:100]}")
```

## Authentication

snowloader supports four auth modes:

```python
# Basic Auth (development)
conn = SnowConnection(instance_url="...", username="...", password="...")

# OAuth Client Credentials (recommended for production)
conn = SnowConnection(instance_url="...", client_id="...", client_secret="...")

# OAuth Password Grant
conn = SnowConnection(instance_url="...", client_id="...", client_secret="...",
                       username="...", password="...")

# Bearer Token
conn = SnowConnection(instance_url="...", token="eyJhbG...")
```

## Links

- [snowloader on PyPI](https://pypi.org/project/snowloader/)
- [snowloader on GitHub](https://github.com/ronidas39/snowloader)
- [Full Documentation](https://snowloader.readthedocs.io)
