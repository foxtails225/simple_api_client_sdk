import os

from dotenv import load_dotenv

load_dotenv()

HUNTER_API_KEY: str = os.getenv("HUNTER_API_KEY", "default_api_key")
BASE_URL: str = "https://api.hunter.io/v2"
