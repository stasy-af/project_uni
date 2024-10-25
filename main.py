import asyncio
from aiogram import Bot, Dispatcher
from handlers import router


BOT_TOKEN='7581394986:AAG23-Xq_TVi1n-4KpFyCyyoh87vR3YqSmA'
bot = Bot(token=BOT_TOKEN)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')