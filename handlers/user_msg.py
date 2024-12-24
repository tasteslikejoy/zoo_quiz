from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from keyboards import reply


router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    try:
        await message.answer(f'Привет, {message.from_user.username}!\n'
                             f'Давай узнает кто твое тотемное животное?',
                             reply_markup=reply.start_kb)
    except Exception as e:
        await message.answer((f'Ошибка:\n'
                              f'{e}'))