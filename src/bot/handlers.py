import logging
from states import *
from bot import *

#Реакция бота на команду /start
@bot.message_handler(commands=['start'])
async def start(message, state: StateContext):
    try:
        await bot.send_message(message.chat.id, 'Привет!\nЯ - чат-бот по мотивации вашей работы!\nПожалуйста, введите ваш логин')
    except Exception as e:
        logging.error(f'/start user:{message.from_user.id} ')