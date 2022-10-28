from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

TOKEN = "5700044308:AAGhzOfSQW0pFt7bWHDsBP9GlHdF47bbt6U"

def echo(update, conext):
    txt = update.message.text
    if txt.lower() in ['привет', 'здарова', 'хай']:
        txt = "привет"
    elif txt.lower() in ['пока', 'пок', 'я ливаю']:
        txt = "пока"
    update.message.reply_text(txt)

    def start(update, conext):
        update.message.reply_text("Вас приветствует ботяра.\nЕсли вы тупой и ничего не понимаете наберите /help")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен!")

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()