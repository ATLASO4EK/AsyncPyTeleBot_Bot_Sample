import asyncio
import logging
from telebot import asyncio_filters
from telebot.states.asyncio.middleware import StateMiddleware

from handlers import *

logging.basicConfig(level=logging.INFO,
                    filename="log.log",
                    filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")

bot.add_custom_filter(asyncio_filters.StateFilter(bot))
bot.setup_middleware(StateMiddleware(bot))
try:
    print('bot started')
    logging.info('bot started')
    asyncio.run(bot.polling())
except Exception as e:
    print(f'bot crashed with exception:\n{e}')
    logging.error(f'bot crashed with exception:\n{e}')