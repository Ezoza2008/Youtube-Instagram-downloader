
import os
import instaloader
from urllib.parse import urlparse

def download_instagram_post(url: str, user_id: str):
    parsed = urlparse(url)
    parts = parsed.path.strip('/').split('/')

    if len(parts) < 2 or parts[0] not in ['p', 'reel']:
        raise ValueError("Faqat 'p' (post) yoki 'reel' URL larni qabul qiladi")

    shortcode = parts[1]

    # ✅ Papkani yaratamiz
    download_dir = os.path.join("downloads", str(user_id))
    os.makedirs(download_dir, exist_ok=True)

    loader = instaloader.Instaloader(
        dirname_pattern=os.path.join(download_dir, shortcode),
        save_metadata=False,
        post_metadata_txt_pattern=""
    )

    try:
        post = instaloader.Post.from_shortcode(loader.context, shortcode)
        loader.download_post(post, target=shortcode)
        print(f"✅ Yuklandi: {shortcode}")
    except Exception as e:
        print(f"❌ Xatolik: {e}")
        raise

    # 📂 Video faylni topamiz
    folder_path = os.path.join(download_dir, shortcode)
    for file in os.listdir(folder_path):
        if file.endswith(".mp4"):
            return os.path.join(folder_path, file)

    raise FileNotFoundError("Video fayl topilmadi")
