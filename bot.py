import telebot
from flask import Flask, request

API_TOKEN = '8238596626:AAHCPswJ-lyH_Hn5Ec_-CFuYxgyazisEDxM'

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Илюша, я тебя люблю 💖")

@app.route(f"/{API_TOKEN}", methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode("utf-8"))
    bot.process_new_updates([update])
    return "ok", 200

@app.route("/", methods=["GET"])
def index():
    return "бот работает", 200

if __name__ == "__main__":
    # Важно: host='0.0.0.0', иначе Render не увидит сервер
    app.run(host='0.0.0.0', port=5000)
