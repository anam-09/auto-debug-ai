import requests
import time


def call_api(
    url: str,
    method: str = "GET",
    payload: dict | None = None,
    headers: dict | None = None,
    retries: int = 2
):
    """
    Generic API caller with logging, HTTP methods, and retry logic.
    """

    method = method.upper()
    headers = headers or {}

    print(f"[API CALL] {method} {url}")

    for attempt in range(retries):
        try:
            response = requests.request(
                method=method,
                url=url,
                json=payload,
                headers=headers,
                timeout=10
            )
            response.raise_for_status()

            print("[API SUCCESS]")
            return {
                "success": True,
                "status_code": response.status_code,
                "data": response.json()
            }

        except Exception as e:
            print(f"[API ERROR] Attempt {attempt + 1}: {e}")

            if attempt == retries - 1:
                return {
                    "success": False,
                    "error": str(e)
                }

            time.sleep(1)