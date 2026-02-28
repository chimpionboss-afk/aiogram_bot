import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.types import Message
from aiogram.filters import Command
# 8536095128:AAFh02t1XYvrePZEYudsOuF0MtbZet8cIw
TOKEN = "8536095128:AAFh02t1XYvrePZEYudsOuF0MtbZet8cIw8"
bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start(messege: Message):
    await messege.answer("assalomu alekom")

@dp.message(F.text)
async def main_kelsa(message: Message):
    await message.answer('siz matin yozyapsiz')


async def main():
    await dp.start_polling(bot)
if __name__=="__main__":
    asyncio.run(main())




                                                                                                               

