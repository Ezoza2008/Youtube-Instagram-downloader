from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

boshmenyu = InlineKeyboardMarkup(row_width=2)
boshmenyu.add(
    InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="uzb"),
    InlineKeyboardButton(text="🇷🇺 Русский", callback_data="rus"),
    InlineKeyboardButton(text="🇺🇸 English", callback_data="eng"),
)

# languages.py


LANGUAGES = {
    "uzb": {
        "lang_selected": "✅ O'zbek tili tanlandi!\n\nEndi bemalol YouTube va Instagram linkini yuboring.",
        "welcome": "Salom, {name}!",
        "choose_language": "Quyidagi tillardan birini tanlang:",
        "downloading": "🔄 Yuklab olish biroz vaqt oladi... Iltimos kuting...",
        "video_downloaded": "✅ Marhamat, videoingiz yuklandi.",
        "file_too_large": "⚠️ Bu video 50MB dan katta. Telegramda yuborib bo‘lmaydi.",
        "error": "⚠️ Xatolik yuz berdi",
        "insta_downloading": "⏳ Instagram post/reels yuklanmoqda...",
        "insta_downloaded": "📥 Instagram post/reels yuklandi✅",
        "insta_file_too_large": "⚠️ Instagram videosi 50MB dan katta. Telegramda yuborilmaydi.",
        "insta_error": "⚠️ Instagramdan yuklab olishda xatolik",
        "invalid_url": "❗ Noto‘g‘ri havola yuborildi. YouTube yoki Instagram URL bo‘lishi kerak."
    },
    "rus": {
        "lang_selected": "✅ Вы выбрали русский язык!\n\nТеперь просто отправьте ссылку на видео с YouTube или Instagram.",
        "welcome": "Здравствуйте, {name}!",
        "choose_language": "Пожалуйста, выберите язык:",
        "downloading": "🔄 Загрузка... Пожалуйста, подождите...",
        "video_downloaded": "✅ Ваше видео загружено.",
        "file_too_large": "⚠️ Видео превышает 50MB. Отправка в Telegram невозможна.",
        "error": "⚠️ Произошла ошибка",
        "insta_downloading": "⏳ Загрузка поста/рила из Instagram...",
        "insta_downloaded": "📥 Пост/рил из Instagram загружен✅",
        "insta_file_too_large": "⚠️ Видео из Instagram превышает 50MB. Отправка в Telegram невозможна.",
        "insta_error": "⚠️ Ошибка при загрузке с Instagram",
        "invalid_url": "❗ Неверная ссылка. Пожалуйста, отправьте ссылку на YouTube или Instagram."
    },
    "eng": {
        "lang_selected": "✅ English has been selected!\n\nNow just send a YouTube or Instagram video link.",
        "welcome": "Hello, {name}!",
        "choose_language": "Please choose a language:",
        "downloading": "🔄 Downloading...It may take a while, please wait...",
        "video_downloaded": "✅ Here is your downloaded video.",
        "file_too_large": "⚠️ The video size exceeds 50MB. Cannot send via Telegram.",
        "error": "⚠️ An error occurred",
        "insta_downloading": "⏳ Downloading Instagram post/reel...",
        "insta_downloaded": "📥 Instagram post/reel downloaded✅",
        "insta_file_too_large": "⚠️ Instagram video exceeds 50MB. Cannot send via Telegram.",
        "insta_error": "⚠️ Failed to download from Instagram",
        "invalid_url": "❗ Invalid URL. Please send a valid YouTube or Instagram link."
    }
}