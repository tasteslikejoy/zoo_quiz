from aiogram import Router
from aiogram.types import Message
from keyboards import reply


router = Router()


@router.message()
async def msg(message: Message):
    msg = message.text.lower()

    if msg == 'начнем опрос':
        await message.answer('Отвечайте на вопросы честно, никто вас не торопит',
                             reply_markup=reply.start_quiz_kb)
    elif msg == 'галя, у нас отмена':
        await message.answer('Ну лан...', reply_markup=reply.start_kb)