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
    ServiceNowCatalogLoader,
    ServiceNowChangeLoader,
    ServiceNowCMDBLoader,
    ServiceNowIncidentLoader,
    ServiceNowKBLoader,
    ServiceNowProblemLoader,
)

__all__ = [
    "ServiceNowIncidentLoader",
    "ServiceNowKBLoader",
    "ServiceNowCMDBLoader",
    "ServiceNowChangeLoader",
    "ServiceNowProblemLoader",
    "ServiceNowCatalogLoader",
]
