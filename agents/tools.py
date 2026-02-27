import requests
import time


def call_api(url: str, retries: int = 2):
    """
    Call any public API with retry logic.
    Returns success flag and data/error.
    """
    for attempt in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return {
                "success": True,
                "data": response.json()
            }
        except Exception as e:
            if attempt == retries - 1:
                return {
                    "success": False,
                    "error": str(e)
                }
            time.sleep(1)