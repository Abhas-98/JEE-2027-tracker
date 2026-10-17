import os
import telebot
from datetime import datetime
import time
import threading
from flask import Flask

# --- WEB SERVER TRICK TO KEEP ONLINE 24/7 ---
app = Flask('')

@app.route('/')
def home():
    return "JEE 2027 Bot is running 24/7!"

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# --- TELEGRAM BOT INITIALIZATION ---
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

# 🔴 CRUCIAL: Put your specific negative JEE 2027 Group ID number below!
GROUP_CHAT_ID =@JEE_PYRAMIDS

def get_countdown_text():
    today = datetime.now()
    target = datetime(2027, 1, 20) # 🎯 JEE 2027 Target Exam Date
    
    difference = target - today
    days_left = difference.days
    weeks_left = days_left // 7
    extra_days = days_left % 7
    
    today_str = today.strftime("%dth %B, %Y")
    
    return (
        "⏳ **JEE Main 2027 Countdown** ⏳\n\n"
        f"📅 Today: {today_str}\n"
        "🎯 Estimated Target: 20th January 2027\n"
        f"⏳ Days Left: {days_left}\n"
        f"📅 Weeks Left: {weeks_left} weeks + {extra_days} days\n\n"
        "Keep going. Every day counts! 🔥"
    )

@bot.message_handler(func=lambda msg: msg.text is not None and msg.text.startswith('/countdown'))
def send_countdown(message):
    response = get_countdown_text()
    bot.send_message(message.chat.id, response)

# --- AUTOMATIC 7:00 AM ALERT MODULE ---
def automatic_scheduler():
    while True:
        # 7:00 AM IST is exactly 1:30 AM UTC time on Render
        current_time = datetime.utcnow()
        if current_time.hour == 1 and current_time.minute == 30:
            if GROUP_CHAT_ID != -1001234567890:
                try:
                    response = get_countdown_text()
                    bot.send_message(chat_id=GROUP_CHAT_ID, text=f"📢 **DAILY MORNING CHECK-IN (JEE 2027)**\n\n{response}")
                except Exception as e:
                    print("Error sending message:", e)
            time.sleep(60)
        time.sleep(10)

if __name__ == "__main__":
    threading.Thread(target=run_dummy_server, daemon=True).start()
    threading.Thread(target=automatic_scheduler, daemon=True).start()
    bot.infinity_polling()
