import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7986523255:AAGsdiYNV1i9-KoJnMqvUxzFWjHoAVN2RG8"

# ایجاد ربات
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    # ایجاد دکمه
    keyboard = InlineKeyboardMarkup()
    channel_button = InlineKeyboardButton(
        text="🎯 عضویت در کانال بهرام احمدی",
        url="https://t.me/rba_ahmadi"
    )
    keyboard.add(channel_button)
    
    # پیام خوش‌آمد
    response = "سلام! به ربات بهرام احمدی خوش آمدید.\n\n"
    response += "برای ارتباط با مدیر و مشاهده محتوا، روی دکمه زیر کلیک کنید:"
    
    bot.send_message(
        chat_id=message.chat.id,
        text=response,
        reply_markup=keyboard
    )

@bot.message_handler(commands=['id'])
def id_command(message):
    bot.reply_to(message, f"آیدی شما: {message.chat.id}")

@bot.message_handler(func=lambda message: True)
def echo(message):
    if "بهرام" in message.text:
        bot.reply_to(message, "👤 برای ارتباط با بهرام احمدی به @rba_ahmadi مراجعه کنید")
    else:
        bot.reply_to(message, "✅ از /start استفاده کنید")

print("🎮 ربات در حال راه‌اندازی...")
print("📞 آیدی کانال: @rba_ahmadi")
print("⚠️ حتما VPN روشن باشد!")
bot.polling()