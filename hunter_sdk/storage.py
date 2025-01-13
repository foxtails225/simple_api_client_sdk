from typing import Dict, List, Optional


class InMemoryStorage:

    def __init__(self) -> None:
        self.storage_cache: Dict[str, Dict[str, str]] = {}

    def save(self, key: str, email_data: Dict[str, str]) -> None:
        self.storage_cache[key] = email_data

    def get(self, key: str) -> Optional[Dict[str, str]]:
        return self.storage_cache.get(key)

    def get_all(self) -> List[Dict[str, str]]:
        return list(self.storage_cache.values())

    def delete(self, key: str) -> None:
        self.storage_cache.pop(key, None)

    def clear(self) -> None:
        self.storage_cache.clear()
