from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from db import dbcreate
from keyboards import reply


router = Router()


@router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await dbcreate.init_db()
    chat_id = message.from_user.id
    username = message.from_user.username

    try:
        user_id = await dbcreate.create_user(chat_id, username)
        if user_id is not None:
            await state.update_data(user_id=user_id)  # Сохраняем user_id в состоянии
            await message.answer(f'Привет, {username}!'
                                 f' Давай узнаем, кто твое тотемное животное?',
                                 reply_markup=reply.start_kb)
        else:
            await message.answer('Не удалось создать пользователя.')

    except Exception as e:
        await message.answer(f'Ошибка: {e}')
