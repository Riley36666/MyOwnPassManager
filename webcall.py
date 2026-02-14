import requests

url = "https://sideproject229.duckdns.org/api/websitecheck"

def webcall():
    try:
        response = requests.post(url, timeout=2)
        if response.status_code == 200 and response.json().get("success") is True:
            return True

        else:
            return False

    except requests.exceptions.RequestException as e:
        print("ERROR:", e)
        return None 


