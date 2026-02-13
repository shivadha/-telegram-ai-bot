import os
import instaloader

DOWNLOAD_PATH = "downloads"

USERNAME = os.environ.get("IG_USERNAME")
PASSWORD = os.environ.get("IG_PASSWORD")

def download_instagram_reel(url: str):
    try:
        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)

        loader = instaloader.Instaloader(
            download_videos=True,
            save_metadata=False
        )

        # Login to Instagram
        if USERNAME and PASSWORD:
            loader.login(USERNAME, PASSWORD)

        shortcode = url.strip("/").split("/")[-1]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        loader.download_post(post, target=DOWNLOAD_PATH)

        return True, "Download successful"

    except Exception as e:
        return False, str(e)
