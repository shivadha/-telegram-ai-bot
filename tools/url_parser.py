
import re

def extract_reel_id(url):
    match = re.search(r"(reel|p)/([^/?]+)", url)
    if match:
        return match.group(2)
    return None
