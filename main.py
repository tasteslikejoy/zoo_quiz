import asyncio
from aiogram import Bot, Dispatcher
from db.dbcreate import init_db
from handlers import bot_msg, user_msg
from config import config
from quiz import quiz, finaly_answer


async def main():
    bot = Bot(config.api_token.get_secret_value())
    dp = Dispatcher()

    dp.include_routers(
        # finaly_answer.router,
        quiz.router,  # должно быть на первом месте
        user_msg.router,
        bot_msg.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())