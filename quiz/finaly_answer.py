# from aiogram import Router, F
# from aiogram.types import Message
# from aiogram.fsm.context import FSMContext
# from db.dbcreate import get_answer_counts, create_or_update_answer_count
# from quiz.quiz import save_results
# from utils import forms
# from keyboards import reply
#
# router = Router()
#
# @router.message(F.text.lower().contains('это будет ле-ген-дарно'))
# async def start_finaly_questions(message: Message, state: FSMContext):
#     user_data = await state.get_data()
#     user_id = user_data.get('user_id')  # Извлекаем user_id
#
#     if user_id is None:
#         await message.answer(f'Пожалуйста, начните с начала.')
#         return
#
#     answer_counts = await get_answer_counts(user_id)
#
#     count_a = answer_counts.get('A', 0)
#     count_b = answer_counts.get('B', 0)
#     count_c = answer_counts.get('C', 0)
#     count_d = answer_counts.get('D', 0)
#
#     if count_a >= max(count_b, count_c, count_d):
#         await message.answer('АУФ?', reply_markup=reply.group_kb)
#         await state.set_state(forms.FormFinaly.one_name_finaly_answer)
#     elif count_b >= max(count_a, count_c, count_d):
#         await message.answer('Я на солнышке лежу?', reply_markup=reply.group_kb)
#         await state.set_state(forms.FormFinaly.two_name_finaly_answer)
#     elif count_c >= max(count_a, count_b, count_d):
#         await message.answer('Вы любите сидеть в засаде?', reply_markup=reply.group_kb)
#         await state.set_state(forms.FormFinaly.three_name_finaly_answer)
#     elif count_d >= max(count_a, count_b, count_c):
#         await message.answer('У вас болит спина?', reply_markup=reply.group_kb)
#         await state.set_state(forms.FormFinaly.four_name_finaly_answer)
#     else:
#         await message.answer('Ваши ответы были разнообразными, но ни один из них не выделяется.')
#
# @router.message(forms.FormFinaly.one_name_finaly_answer)
# async def one_name_finaly_answer(message: Message, state: FSMContext):
#     user_response = message.text.lower()
#     await save_results(state, 'А', user_response)  # Сохраняем ответ
#     user_data = await state.get_data()  # Получаем данные состояния
#     user_id = user_data.get('user_id')  # Извлекаем user_id
#
#     # Получаем текущее количество ответов для 'А'
#     answer_counts = await get_answer_counts(user_id)
#     count_a = answer_counts.get('A', 0) + 1  # Увеличиваем счетчик на 1
#
#     await create_or_update_answer_count(user_id, 'А', count_a)  # Обновляем счетчик ответов
#
#     if user_response in ['да', 'yes']:
#         await message.answer("Вы волк!")
#     elif user_response in ['нет', 'no']:
#         await message.answer("Вы шакал!")
#     else:
#         await message.answer("Пожалуйста, ответьте 'да' или 'нет'.")
#
#
# @router.message(forms.FormFinaly.two_name_finaly_answer)
# async def two_name_finaly_answer(message: Message, state: FSMContext):
#     user_response = message.text.lower()
#     await save_results(state, 'Б', user_response)
#     user_data = await state.get_data()  # Получаем данные состояния
#     user_id = user_data.get('user_id')
#     await create_or_update_answer_count(user_id, 'Б')  # Обновляем счетчик ответов
#
#     if user_response in ['да', 'yes']:
#         await message.answer("Вы черепаха!")
#     elif user_response in ['нет', 'no']:
#         await message.answer("Вы морж!")
#     else:
#         await message.answer("Пожалуйста, ответьте 'да' или 'нет'.")
#
# @router.message(forms.FormFinaly.three_name_finaly_answer)
# async def three_name_finaly_answer(message: Message, state: FSMContext):
#     user_response = message.text.lower()
#     await save_results(state, 'В', user_response)
#     user_data = await state.get_data()  # Получаем данные состояния
#     user_id = user_data.get('user_id')
#     # Сохраняем ответ
#     await create_or_update_answer_count(user_id, 'В')  # Обновляем счетчик ответов
#
#     if user_response in ['да', 'yes']:
#         await message.answer("Вы китоглав!")
#     elif user_response in ['нет', 'no']:
#         await message.answer("Вы аист!")
#     else:
#         await message.answer("Пожалуйста, ответьте 'да' или 'нет'.")
#
# @router.message(forms.FormFinaly.four_name_finaly_answer)
# async def four_name_finaly_answer(message: Message, state: FSMContext):
#     user_response = message.text.lower()
#     await save_results(state, 'Г', user_response)
#     user_data = await state.get_data()  # Получаем данные состояния
#     user_id = user_data.get('user_id')
#     await create_or_update_answer_count(user_id, 'Г')  # Обновляем счетчик ответов
#
#     if user_response in ['да', 'yes']:
#         await message.answer("Вы крокодил!")
#     elif user_response in ['нет', 'no']:
#         await message.answer("Вы анаконда!")
#     else:
#         await message.answer("Пожалуйста, ответьте 'да' или 'нет'.")