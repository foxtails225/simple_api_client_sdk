
from typing import Any, Dict, List, Optional

import requests

from hunter_sdk.config import BASE_URL, HUNTER_API_KEY
from hunter_sdk.storage import InMemoryStorage

HTTP_OK: int = 200


class HunterService:

    def __init__(self, storage: Optional[InMemoryStorage] = None) -> None:
        self.storage = storage or InMemoryStorage()

    def validate_email(self, email: str) -> Dict[str, Any]:
        url: str = f"{BASE_URL}/email-verifier"
        request_parameters: Dict[str, str] = {"email": email, "api_key": HUNTER_API_KEY}
        response = requests.get(url, params=request_parameters, timeout=10)
        response_data: Dict[str, Any] = response.json()

        if response.status_code == HTTP_OK:
            self.storage.save(email, response_data)
            return response_data
        raise Exception(f"Failed to fetch data: {response_data}")

    def find_emails_by_domain(self, domain: str) -> Dict[str, Any]:
        url: str = f"{BASE_URL}/domain-search"
        request_parameters: Dict[str, str] = {"domain": domain, "api_key": HUNTER_API_KEY}
        response = requests.get(url, params=request_parameters, timeout=10)
        response_data: Dict[str, Any] = response.json()

        if response.status_code == HTTP_OK:
            self.storage.save(domain, response_data)
            return response_data
        raise Exception(f"Failed to fetch data: {response_data}")

    def find_email(self, first_name: str, last_name: str, company_domain: str) -> Dict[str, Any]:
        url: str = f"{BASE_URL}/email-finder"
        request_parameters: Dict[str, str] = {
            "first_name": first_name,
            "last_name": last_name,
            "domain": company_domain,
            "api_key": HUNTER_API_KEY,
        }
        response = requests.get(url, params=request_parameters, timeout=10)
        response_data: Dict[str, Any] = response.json()

        if response.status_code == HTTP_OK:
            email_key = f"{first_name}.{last_name}@{company_domain}"
            self.storage.save(email_key, response_data)
            return response_data
        raise Exception(f"Failed to fetch data: {response_data}")

    def get_cached_email(self, email: str) -> Optional[Dict[str, Any]]:
        return self.storage.get(email)

    def get_all_cached_emails(self) -> List[Dict[str, str]]:
        return self.storage.get_all()
