
import threading
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler , Filters
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, ChatMemberUpdated
from telegram import KeyboardButton, ReplyKeyboardMarkup
import logging
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 5000))


bot_token = "5303668300:AAETnkAJLDBvK9KI3r6A9s50Gw_2U5omZUg"

bot = telegram.Bot(token=bot_token)



def Start(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]
    markup= ReplyKeyboardMarkup([[KeyboardButton("/info"), KeyboardButton("/packages"),] ], resize_keyboard=True)
    context.bot.send_message(chat_id=chat_id,text = f"Welcome to oathub bootcamp, {first_name}. Know more about us by clicking on the function buttons below", reply_markup = markup)
   

def Info(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]

    messages = f"We are a group of tech brothers ready to invest knowledge in the lives of many. We are offering courses in the field of web development, graphics design and crypto"
    photo = "https://oathub-385f7.web.app/img/oat.1a04ffc9.jpg"
    context.bot.send_photo(chat_id=chat_id, caption=messages , photo=photo)

def Package(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]
    context.bot.send_message(chat_id=chat_id,text=f" Our packages are quite cheap and offered within three months: \n\n 1. Web Development at NGN20,000 \n\n 2. Graphics design at NGN15,000 \n\n 3. Cryto Trading at NGN30,000 \n\n \n\n \n\n \n\n To register and make payments visit our website: https://oathub-385f7.web.app/ ")

def echo(update, context):

    thread = threading.Thread(target= Welcome, args=[update, context])

    thread.start()

def main():
    
    updater=Updater("5303668300:AAETnkAJLDBvK9KI3r6A9s50Gw_2U5omZUg" ,use_context=True)

    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",Start))
    dp.add_handler(CommandHandler("info",Info))
    dp.add_handler(CommandHandler("packages",Package))
    

    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=bot_token,
                            webhook_url='https://oathubbot.herokuapp.com/ ' + bot_token)
    
    #updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
    