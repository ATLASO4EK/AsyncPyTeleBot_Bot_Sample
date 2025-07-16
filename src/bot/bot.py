from config import get_token
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage

bot = AsyncTeleBot(get_token(), state_storage=StateMemoryStorage())