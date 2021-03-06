
import threading
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler , Filters
from telegram import  InlineKeyboardButton, InlineKeyboardMarkup, ChatMemberUpdated
from telegram import KeyboardButton, ReplyKeyboardMarkup
import logging
import os
import json 
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

PORT = int(os.environ.get('PORT', 5000))


bot_token = "5303668300:AAETnkAJLDBvK9KI3r6A9s50Gw_2U5omZUg"

bot = telegram.Bot(token=bot_token)

config = json.load(open("config.json"))

def Start(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["from_user"]["first_name"]
    username = update["message"]["from_user"]["username"]
    markup= ReplyKeyboardMarkup([[KeyboardButton("/info"), KeyboardButton("/packages"),KeyboardButton("/contact"),KeyboardButton("/instructors"),KeyboardButton("/FAQ")] ], resize_keyboard=True)
    context.bot.send_message(chat_id=chat_id,text = f"Welcome to oathub bootcamp, {first_name}. Know more about us by clicking on the function buttons below", reply_markup = markup)
   


def menu(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(
        chat_id=chat_id, text=config["messages"]["menu"])

def Info(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]

    messages = f"oathub is a growing media startup. We are here to improve the tech life of individuals. "
    photo = "https://oathub-385f7.web.app/img/oat.1a04ffc9.jpg"
    context.bot.send_photo(chat_id=chat_id, caption=messages , photo=photo)


def instructors(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]

    messages = f"Contact the instructors: \n\n Bishop Olugbenga <b> (Graphic Designer)</b> \n 08109479682 \n\n Iyanuoluwa Akinwumi <b> (Web Developer) </b> \n 07065487342 \n\n Opeyemi Akinwumi <b> (Technical Analyst) </b> \n 08131567097 "
    photo = "https://oathub-385f7.web.app/img/oat.1a04ffc9.jpg"
    context.bot.send_message(chat_id=chat_id, text= messages,parse_mode=telegram.ParseMode.HTML )


def FAQ(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]

    messages = f" 1. How experienced are the insructors? \n\n <b> Ans: Each instructor has over 3 years of professional experience. </b> \n\n 2. Can I register for more than a course? \n\n <b> Ans: Yes, you can register for more than a course. All you have to do is pay online, we will be notified and you will be directed to the main telegram group </b> \n\n 3. I have no experience in tech, can I apply? \n\n <b> Ans: Yes! You can. In fact, this bootcamp is meant for you. </b> \n\n"
    photo = "https://oathub-385f7.web.app/img/oat.1a04ffc9.jpg"
    context.bot.send_message(chat_id=chat_id, text= messages ,parse_mode=telegram.ParseMode.HTML)




def Package(update,context):
    chat_id = update.effective_chat.id
    first_name = update["message"]["chat"]["first_name"]
    username = update["message"]["chat"]["username"]
    context.bot.send_message(chat_id=chat_id,text=f" Our packages are quite affordable, and offered within 8 weeks: \n\n 1. Graphic Design at NGN15,000 \n\n 2. Web Development at NGN15,000 \n\n 3. Cryto Trading at NGN15,000 \n\n \n\n \n\n \n\n To register and make payments visit our website: https://bit.ly/oathub-bootcamp")

def Contact(update,context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id,text="Contact info: \n\n Mail: oathub@outlook.com")

def main():
    
    updater=Updater("5303668300:AAETnkAJLDBvK9KI3r6A9s50Gw_2U5omZUg" ,use_context=True)

    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start",Start))
    dp.add_handler(CommandHandler("info",Info))
    dp.add_handler(CommandHandler("packages",Package))
    dp.add_handler(CommandHandler("contact",Contact))
    dp.add_handler(CommandHandler("menu",menu))
    dp.add_handler(CommandHandler("instructors",instructors))
    dp.add_handler(CommandHandler("FAQ",FAQ))
   

    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=bot_token, webhook_url='https://oatbott.herokuapp.com/' + bot_token)
    #updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
    