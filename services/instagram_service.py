import os
import instaloader

DOWNLOAD_PATH = "downloads"

def download_instagram_reel(url: str):
    try:
        if not os.path.exists(DOWNLOAD_PATH):
            os.makedirs(DOWNLOAD_PATH)

        loader = instaloader.Instaloader(download_videos=True, save_metadata=False)

        shortcode = url.strip("/").split("/")[-1]
        post = instaloader.Post.from_shortcode(loader.context, shortcode)

        loader.download_post(post, target=DOWNLOAD_PATH)

        return True, "Download successful"
    except Exception as e:
        return False, str(e)
