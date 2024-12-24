from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.forms import Form
from keyboards import reply


router = Router()


answer_count = {
    'А': 0,
    'Б': 0,
    'В': 0,
    'Г': 0,
}

@router.message(F.text.lower().contains('приступим'))
async def start_quiz(message: Message, state: FSMContext):
    await state.set_state(Form.one_name_answer)
    await message.answer('Что бы принять важное решение, '
                         'каким правилом вы руководствуетесь?',
                         reply_markup=reply.one_q_kb)


@router.message(Form.one_name_answer)
async def one_name_answer(message: Message, state: FSMContext):
    await state.update_data(one_name_answer=message.text)
    answer = message.text.split(' ')[0].strip('.').upper()

    if answer in answer_count:
        # await message.answer(f'Ваш ответ: {answer}')
        answer_count[answer] += 1

    await state.set_state(Form.two_name_answer)
    await message.answer('Кто вы в этой жизни?', reply_markup=reply.two_q_kb)

@router.message(Form.two_name_answer)
async def two_name_answer(message: Message, state: FSMContext):
    await state.update_data(two_name_answer=message.text)
    answer = message.text.split(' ')[0].strip('.').upper()

    if answer in answer_count:
        answer_count[answer] += 1

    await state.set_state(Form.three_name_answer)
    await message.answer('Что вы хотите от жизни?', reply_markup=reply.three_q_kb)


