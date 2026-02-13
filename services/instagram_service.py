import requests

def fetch_instagram_metadata(url: str):
    try:
        oembed_url = "https://graph.facebook.com/v17.0/instagram_oembed"

        params = {
            "url": url,
            "access_token": None  # we will add later if needed
        }

        response = requests.get(oembed_url, params={"url": url})

        if response.status_code == 200:
            data = response.json()
            return True, data
        else:
            return False, f"Failed with status {response.status_code}"

    except Exception as e:
        return False, str(e)
