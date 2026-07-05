import requests
from urllib.parse import quote


def fact_check(query: str) -> str:
    """
    Fetch a short summary from Wikipedia using the official REST API.
    """

    try:
        encoded_query = quote(query)
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_query}"

        response = requests.get(
            url,
            headers={
                "User-Agent": "PersonalizedNetworkingAssistant/1.0"
            },
            timeout=10
        )

        if response.status_code != 200:
            return "No information found."

        data = response.json()

        return data.get("extract", "No summary available.")

    except Exception as e:
        return f"Fact-checking failed: {e}"