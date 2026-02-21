import requests
from src.version import __version__ as current_version

GITHUB_API = "https://api.github.com/repos/Riley36666/MyOwnPassManager/releases/latest"

def updateChecker():
    try:
        res = requests.get(GITHUB_API, timeout=10)
        res.raise_for_status()
        latest = res.json()["tag_name"]
        if latest != current_version:
            print(f"Update available: {latest} (you have {current_version})")
        else:
            print("Up to date")
    except Exception as e:
        print(f"Update check failed: {e}")
