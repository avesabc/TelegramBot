import asyncio
from aiogram import Bot, Dispatcher, types


# bot - server using with API telegram
TOKEN_API = "7911390712:AAFSul6obssbL40mZKvqrMK4721iTLa_Eb8" # autorizaithon token

bot = Bot(TOKEN_API)
dp = Dispatcher()



@dp.message()
async def echo(message: types.Message):
    await message.answer(text=message.text) # answer to message

async def main():
    await dp.start_polling(bot)

# nested
if __name__ == '__main__':
    asyncio.run(main())
