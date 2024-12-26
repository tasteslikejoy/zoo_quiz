import asyncio
import time
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from db.dbcreate import create_or_update_answer_count
from utils.forms import Form, FormFinaly
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
    await message.answer('Что бы принять важное решение,'
                         'каким правилом вы руководствуетесь?',
                         reply_markup=reply.one_q_kb)

@router.message(Form.one_name_answer)
async def one_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.two_name_answer, 'Кто вы в этой жизни?', reply.two_q_kb)

@router.message(Form.two_name_answer)
async def two_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.three_name_answer, 'Что вы хотите от жизни?', reply.three_q_kb)

@router.message(Form.three_name_answer)
async def three_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.four_name_answer, 'Какой вариант подходим вам больше?', reply.four_q_kb)

@router.message(Form.four_name_answer)
async def four_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.five_name_answer, 'Что больше всего вас привлекает?', reply.five_q_kb)

@router.message(Form.five_name_answer)
async def five_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.six_name_answer, 'Чего вы больше всего боитесь?', reply.six_q_kb)

@router.message(Form.six_name_answer)
async def six_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.seven_name_answer, 'Вашей отличительной чертой является', reply.seven_q_kb)

@router.message(Form.seven_name_answer)
async def seven_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.eight_name_answer, 'Без чего вы не можете обойтись?', reply.eight_q_kb)

@router.message(Form.eight_name_answer)
async def eight_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.nine_name_answer, 'Какая ваша мечта?', reply.nine_q_kb)

@router.message(Form.nine_name_answer)
async def nine_name_answer(message: Message, state: FSMContext):
    await process_answer(message, state, Form.ten_name_answer, 'Какое качество вы бы хотели в себе развить?', reply.ten_q_kb)

@router.message(Form.ten_name_answer)
async def ten_name_answer(message: Message, state: FSMContext):
    await state.update_data(ten_name_answer=message.text)
    answer = message.text.split(' ')[0].strip('.').upper()

    if answer in answer_count:
        answer_count[answer] += 1

    results = ' '.join([f'{key}: {value}' for key, value in answer_count.items()])
    max_answer = max(answer_count, key=answer_count.get)
    max_value = answer_count[max_answer]

    await message.answer(f'Ваши ответы: {results}\n'
                         f'Наиболее популярный ответ: {max_answer} ({max_value} раз(а))\n\n')
                         # f'ВЫ ГОТОВЫ К ФИНАЛЬНОМУ ВОПРОСУ?', reply_markup=reply.finaly_kb)

    await save_results(state, answer, answer_count[answer])

    time.sleep(5)

    if answer_count['А'] > answer_count['Б'] and answer_count['А'] > answer_count['В'] and answer_count['А'] > answer_count['Г']:
        await message.answer('Ауф?', reply_markup=reply.group_kb)
        await state.set_state(FormFinaly.one_name_finaly_answer)

    elif answer_count['Б'] > answer_count['А'] and answer_count['Б'] > answer_count['В'] and answer_count['Б'] > answer_count['Г']:
        await message.answer('Я на солнышке лежу?', reply_markup=reply.group_kb)
        await state.set_state(FormFinaly.two_name_finaly_answer)

    elif answer_count['В'] > answer_count['А'] and answer_count['В'] > answer_count['Б'] and answer_count['В'] > answer_count['Г']:
        await message.answer('Вы любите сидеть в засаде?', reply_markup=reply.group_kb)
        await state.set_state(FormFinaly.three_name_finaly_answer)

    elif answer_count['Г'] > answer_count['А'] and answer_count['Г'] > answer_count['Б'] and answer_count['Г'] > answer_count['В']:
        await message.answer('У вас болит спина?', reply_markup=reply.group_kb)
        await state.set_state(FormFinaly.four_name_finaly_answer)

    @router.message(FormFinaly.one_name_finaly_answer)
    async def final_question_a(message: Message, state: FSMContext):

        if message.text.lower() in ['да', 'yes']:
            await message.answer('Поздравляем! Вы волк!')
        else:
            await message.answer('Вы шакал!')

        await state.clear()

    @router.message(FormFinaly.two_name_finaly_answer)
    async def final_question_b(message: Message, state: FSMContext):

        if message.text.lower() in ['да', 'yes']:
            await message.answer('Вы черепаха!')
        else:
            await message.answer('Вы морж!')

        await state.clear()

    @router.message(FormFinaly.three_name_finaly_answer)
    async def final_question_v(message: Message, state: FSMContext):

        if message.text.lower() in ['да', 'yes']:
            await message.answer('Вы китоглав!')
        else:
            await message.answer('Вы аист!')

        await state.clear()

    @router.message(FormFinaly.four_name_finaly_answer)
    async def final_question_g(message: Message, state: FSMContext):

        if message.text.lower() in ['да', 'yes']:
            await message.answer('Вы крокодил!')
        else:
            await message.answer('Вы анаконда!')

        await state.clear()

async def process_answer(message: Message, state: FSMContext, next_state, question, reply_markup):
    current_state = await state.get_state()
    await state.update_data(**{current_state: message.text})
    answer = message.text.split(' ')[0].strip('.').upper()

    if answer in answer_count:
        answer_count[answer] += 1
        user_data = await state.get_data()
        user_id = user_data.get('user_id')

        if user_id is not None:
            count = answer_count[answer]
            await create_or_update_answer_count(user_id, answer, count)

    await state.set_state(next_state)
    await message.answer(question, reply_markup=reply_markup)



async def save_results(state: FSMContext, answer: str, count: int):
    user_data = await state.get_data()
    user_id = user_data.get('user_id')

    if user_id is not None:
        await create_or_update_answer_count(user_id, answer, count)

