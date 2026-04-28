"""ServiceNow document loaders for LangChain, powered by snowloader.

Provides six loaders covering the core ServiceNow tables, each producing
LangChain Documents ready for any vector store, retriever, or chain.

Usage:
    from langchain_snowloader import ServiceNowIncidentLoader
    from snowloader import SnowConnection

    conn = SnowConnection(instance_url="...", username="...", password="...")
    loader = ServiceNowIncidentLoader(connection=conn, query="active=true")
    docs = loader.load()
"""

from snowloader.adapters.langchain import (
    ServiceNowAttachmentLoader,
    ServiceNowCatalogLoader,
    ServiceNowChangeLoader,
    ServiceNowCMDBLoader,
    ServiceNowIncidentLoader,
    ServiceNowKBLoader,
    ServiceNowProblemLoader,
)

# Async variants are re-exported when aiohttp is installed alongside snowloader.
try:
    from snowloader.adapters.langchain import (  # noqa: F401
        AsyncServiceNowAttachmentLoader,
        AsyncServiceNowCatalogLoader,
        AsyncServiceNowChangeLoader,
        AsyncServiceNowCMDBLoader,
        AsyncServiceNowIncidentLoader,
        AsyncServiceNowKBLoader,
        AsyncServiceNowProblemLoader,
    )

    _ASYNC_EXPORTS = [
        "AsyncServiceNowAttachmentLoader",
        "AsyncServiceNowCatalogLoader",
        "AsyncServiceNowChangeLoader",
        "AsyncServiceNowCMDBLoader",
        "AsyncServiceNowIncidentLoader",
        "AsyncServiceNowKBLoader",
        "AsyncServiceNowProblemLoader",
    ]
except ImportError:
    _ASYNC_EXPORTS = []

__all__ = [
    "ServiceNowAttachmentLoader",
    "ServiceNowIncidentLoader",
    "ServiceNowKBLoader",
    "ServiceNowCMDBLoader",
    "ServiceNowChangeLoader",
    "ServiceNowProblemLoader",
    "ServiceNowCatalogLoader",
    *_ASYNC_EXPORTS,
]
