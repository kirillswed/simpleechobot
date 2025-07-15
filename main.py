import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv("token")

dp = Dispatcher()



@dp.message(F.text)
async def echo_handler(message: Message):
    await message.answer(message.text)

@dp.message(F.sticker)
async def echo_handler(message: Message):
    await message.answer(message.sticker)



async def main():
    bot = Bot(API_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())