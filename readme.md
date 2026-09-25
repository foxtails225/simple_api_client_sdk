# Hunter SDK

A lightweight, fully typed Python client for the [Hunter.io API](https://hunter.io/api-documentation). It wraps three endpoints behind a small service class and caches every successful response so repeated lookups don't spend API credits.

- Verify whether an email address is deliverable (`/email-verifier`)
- Find the emails associated with a domain (`/domain-search`)
- Find a person's professional email from their name and company domain (`/email-finder`)
- Cache responses through a pluggable storage class (in-memory by default)

## Installation

```sh
git clone https://github.com/foxtails225/simple_api_client_sdk.git
cd simple_api_client_sdk
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
```

Create a `.env` file with your API key:

```
HUNTER_API_KEY=your_api_key
```

## Usage

```python
from hunter_sdk.service import HunterService

hunter = HunterService()

result = hunter.validate_email("jane@example.com")
print(result["data"]["status"])

domain = hunter.find_emails_by_domain("example.com")
person = hunter.find_email("Jane", "Doe", "example.com")

# Cached results, no extra API calls
hunter.get_cached_email("jane@example.com")
hunter.get_all_cached_emails()
```

Any non-200 response raises an exception that includes the API's error payload. Requests time out after 10 seconds.

### Custom storage

`HunterService` accepts any storage object that has `save`, `get` and `get_all` methods, so the in-memory cache can be swapped for Redis, a database, or a file:

```python
from hunter_sdk.service import HunterService
from hunter_sdk.storage import InMemoryStorage

hunter = HunterService(storage=InMemoryStorage())
```

## Project structure

```
hunter_sdk/
  service.py   HunterService: API calls and caching
  storage.py   InMemoryStorage: save / get / get_all / delete / clear
  config.py    API key (from .env) and base URL
tests/
  test_service.py
```

## Tests and code quality

```sh
pytest
mypy hunter_sdk
flake8 hunter_sdk
```

The code is type-checked with strict mypy settings (`disallow_untyped_defs`, `strict_optional`, `warn_unreachable`) and linted with flake8 plus wemake-python-styleguide. See `setup.cfg` for the full configuration.
