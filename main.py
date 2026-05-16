from telebot.async_telebot import AsyncTeleBot
from telebot import types
from keyboards import *
from keyboards import LANGUAGES
from downloader import download_instagram_post
import asyncio
import yt_dlp
import os
import json


first_messages = {}

def load_langs():
    try:
        with open('user_langs.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_langs(data):
    with open('user_langs.json', 'w') as f:
        json.dump(data, f)

user_langs = load_langs()

# ✅ CORRECT — works both locally and on Choreo
bot = AsyncTeleBot(
    token=os.environ.get("BOT_TOKEN", "8699298904:AAEKppKxz_JZkWal_uSyetmv-BhycgUsUx0")
)
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50 MB

@bot.message_handler(commands=["start"])
async def boshfunksiya(message: types.Message):
    user_langs[message.chat.id] = "uzb"  # Default til
    lang = LANGUAGES.get(user_langs.get(str(message.chat.id), "uzb"))

    first_word = await bot.send_message(message.chat.id, lang["welcome"].format(name=message.from_user.full_name))
    first_messages[str(message.chat.id)] = first_word.message_id 
    
    
    await bot.send_message(message.chat.id, lang["choose_language"], reply_markup=boshmenyu)
    

@bot.callback_query_handler(lambda c: c.data in ["uzb", "rus", "eng"])
async def inlinetugmacha(callback: types.CallbackQuery):
    await bot.answer_callback_query(callback.id)
    
    chat_id = callback.message.chat.id
    message_id = callback.message.message_id
    user_langs[str(chat_id)] = callback.data  # Foydalanuvchining tilini saqlaymiz
    lang = LANGUAGES[callback.data]  # str bo'lishi kerak JSON uchun
    save_langs(user_langs)

    await bot.edit_message_text(
                chat_id=chat_id,
                message_id=first_messages[str(chat_id)],
                text=lang["welcome"].format(name=callback.from_user.full_name)
            )
    
    await bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=lang["lang_selected"].format(name=callback.from_user.first_name))


# YouTube video yuklab beruvchi funksiya
def download_video(url):
    ydl_opts = {
        'format': '18',
        'outtmpl': 'video.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'retries': 3,
        'concurrent_fragment_downloads': 5,
        'fragment_retries': 5,
        'writesubtitles': True,
        'writeautomaticsub': True,
         'cookiefile': 'cookies.txt',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        return filename

# YouTube va Instagram linklarini qabul qiluvchi handler
@bot.message_handler(content_types=["text"])
async def link_qabul_qilish(message: types.Message):
    url = message.text.strip()
    lang = LANGUAGES.get(user_langs.get(str(message.chat.id), "uzb"))


    if "youtube.com" in url or "youtu.be" in url:
        loading_msg = await bot.send_message(message.chat.id, lang["downloading"])
        try:
            file_path = download_video(url)
            if os.path.getsize(file_path) > MAX_FILE_SIZE:
                await bot.send_message(message.chat.id, lang["file_too_large"])
                os.remove(file_path)
                return
            with open(file_path, 'rb') as video:
                await bot.send_video(message.chat.id, video=video)
            await bot.delete_message(chat_id=message.chat.id, message_id=loading_msg.message_id)
            await bot.send_message(message.chat.id, lang["video_downloaded"])
            os.remove(file_path)
        except Exception as e:
            await bot.send_message(message.chat.id, f"{lang['error']}: {e}")

    elif "instagram.com" in url:
        loading_msg1 = await bot.send_message(message.chat.id, lang["insta_downloading"])
        try:
            file_pathinst = download_instagram_post(message.text, f"{message.chat.id}")
            if os.path.getsize(file_pathinst) > MAX_FILE_SIZE:
                await bot.send_message(message.chat.id, lang["insta_file_too_large"])
                os.remove(file_pathinst)
                return
            with open(file_pathinst, 'rb') as video:
                await bot.send_video(message.chat.id, video=video)
            await bot.send_message(message.chat.id, lang["insta_downloaded"])
            os.remove(file_pathinst)
        except Exception as e:
            await bot.send_message(message.chat.id, f"{lang['insta_error']}: {e}")
        finally:
            await bot.delete_message(chat_id=message.chat.id, message_id=loading_msg1.message_id)

    else:
        await bot.send_message(message.chat.id, lang["invalid_url"])


async def main():
    await bot.polling(skip_pending=True)

asyncio.run(main())