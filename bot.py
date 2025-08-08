import telebot
from flask import Flask, request

TOKEN = '8238596626:AAHCPswJ-lyH_Hn5Ec_-CFuYxgyazisEDxM'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Илюша, я тебя люблю 💖")

@app.route(f'/{TOKEN}', methods=['POST'])
def getMessage():
    bot.process_new_messages([telebot.types.Update.de_json(request.stream.read().decode("utf-8")).message])
    return "!", 200

@app.route('/')
def index():
    return "Бот запущен!", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
