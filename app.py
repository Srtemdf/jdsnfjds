
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import os
from dotenv import load_dotenv

load_dotenv()

# Конфигурация через переменные окружения
TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
GROUP_ID = int(os.getenv('GROUP_ID'))

bot = Bot(token=TOKEN)
dp = Dispatcher()

signals = {}
usernames = {}

class SignalStates(StatesGroup):
    waiting_for_signal_text = State()

# Далее твой код хендлеров и клавиатур полностью как ты прислал — его нужно будет дополнить вручную

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
