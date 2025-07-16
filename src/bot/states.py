from telebot.asyncio_handler_backends import State, StatesGroup
from telebot.states.sync.context import StateContext

class States(StatesGroup):
    login = State()