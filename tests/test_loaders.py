"""Tests for the langchain-snowloader package."""

from langchain_snowloader import (
    ServiceNowCatalogLoader,
    ServiceNowChangeLoader,
    ServiceNowCMDBLoader,
    ServiceNowIncidentLoader,
    ServiceNowKBLoader,
    ServiceNowProblemLoader,
)


def test_all_loaders_importable() -> None:
    """All six loader classes should be importable from the package."""
    loaders = [
        ServiceNowIncidentLoader,
        ServiceNowKBLoader,
        ServiceNowCMDBLoader,
        ServiceNowChangeLoader,
        ServiceNowProblemLoader,
        ServiceNowCatalogLoader,
    ]
    assert len(loaders) == 6
