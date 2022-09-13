import config
import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot, storage=storage)
