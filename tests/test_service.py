import pytest
from hunter_sdk.service import HunterService
from hunter_sdk.storage import InMemoryStorage


@pytest.fixture
def storage():
    return InMemoryStorage()


@pytest.fixture
def service(storage):
    return HunterService(storage)


def test_storage_save_and_get(storage):
    storage.save("test@example.com", {"status": "valid"})
    assert storage.get("test@example.com") == {"status": "valid"}


def test_storage_delete(storage):
    storage.save("test@example.com", {"status": "valid"})
    storage.delete("test@example.com")
    assert storage.get("test@example.com") is None


def test_service_caching(service):
    email = "test@example.com"
    service.storage.save(email, {"status": "valid"})
    assert service.get_cached_email(email) == {"status": "valid"}
