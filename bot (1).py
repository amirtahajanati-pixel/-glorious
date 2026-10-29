import os
import telebot
from telebot import types

# Set your NEW bot token in the Windows Command Prompt before running:
# set TELEGRAM_BOT_TOKEN=YOUR_NEW_TOKEN
TOKEN = os.getenv("9171457804:AAEc0Pz9LCVUj7WE7yGTE9CKzs_i3K5QM3Q")

if not TOKEN:
    raise SystemExit(
        "Bot token not set. In CMD, run:
"
        "set TELEGRAM_BOT_TOKEN=YOUR_NEW_TOKEN
"
        "Then run: python bot.py"
    )

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True
    )
    markup.row("🇮🇷 Persian", "🇬🇧 English")

    bot.send_message(
        message.chat.id,
        "Hello! Please choose a language:",
        reply_markup=markup
    )


@bot.message_handler(
    func=lambda message: message.text in ["🇮🇷 Persian", "🇬🇧 English"]
)
def choose_language(message):
    if message.text == "🇮🇷 Persian":
        text = (
            "✅ زبان فارسی انتخاب شد! 🎉\n"
            "به ربات خوش آمدید.\n\n"
            "دستورات:\n"
            "/start — شروع مجدد"
        )
    else:
        text = (
            "✅ English selected! 🎉\n"
            "Welcome to the bot.\n\n"
            "Commands:\n"
            "/start — Restart"
        )

    bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
