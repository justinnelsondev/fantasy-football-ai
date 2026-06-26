import requests

BASE_URL = "https://api.sleeper.app/v1"


def get_league(league_id):
    response = requests.get(f"{BASE_URL}/league/{league_id}")
    response.raise_for_status()
    return response.json()