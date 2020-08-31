from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import asyncio

from bin.config import bot_token, database_name, parse_mode
from bin.settings_class import SQLite_db, Scheduler_ex, Middleware

# Loop
loop = asyncio.get_event_loop()

# Scheduler
scheduler = Scheduler_ex(loop)

# MemoryStorage
storage = MemoryStorage()

# Bot
bot = Bot(token=bot_token, loop=loop, parse_mode=parse_mode)

# Dispatcher
dp = Dispatcher(bot, storage=storage, loop=loop)

# Database
db = SQLite_db(db='bin\{}.db'.format(database_name))
dp.middleware.setup(Middleware(db))
