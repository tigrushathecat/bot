from telegram import ForceReply, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from Models.сard import *
from Models.user import *

import random

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = ReplyKeyboardMarkup(keyboard=[["Получить карточку", "Донат",'Моя Коллекция']])
    id = update.message.from_user.id
    name = update.message.from_user.first_name
    surname = update.message.from_user.last_name
    nick = update.message.from_user.username
    all_users.update({id: User(id, name, surname, nick)})
    await update.message.reply_text(text = "Привет я друг", reply_markup=keyboard)



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")


async def messages_main_function(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    user = all_users.get(update.message.from_user.id)
    if text == 'Получить карточку':
        test_card = random.choice(all_cards_list)
        user.add_card(test_card)
        await update.message.reply_photo(photo=test_card.pic_url, caption=test_card.show_card())
    if text == 'Моя Коллекция':
        await update.message.reply_text(user.get_cards_collection_names())




application = Application.builder().token("7414476554:AAE9SrXZBQSt29caLazLK0i0NsHDht86eNw").build()
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, messages_main_function))
application.run_polling(allowed_updates=Update.ALL_TYPES)


