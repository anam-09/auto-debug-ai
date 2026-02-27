import requests


def call_api(url: str):
    """
    Calls a public API and returns JSON response.
    Raises an error if request fails.
    """
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()