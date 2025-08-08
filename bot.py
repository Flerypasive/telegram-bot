from flask import Flask, request
import telebot
import os

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Илюша, я тебя люблю 💖")

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = telebot.types.Update.de_json(request.data.decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200

@app.route('/')
def index():
    return "Бот работает!"

if __name__ == "__main__":
    app.run()