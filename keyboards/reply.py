from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Начнем опрос'),
            KeyboardButton(text='Интересный факт')
        ],
        [
            KeyboardButton(text='Узнать о программе опеки')
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='АУФ...'  # TODO добавить вывод мемов про волков
)

start_quiz_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Приступим'),
            KeyboardButton(text='ГАЛЯ, У НАС ОТМЕНА')
        ]
    ],
    resize_keyboard=True
)

one_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Ой, будь что будет...')
        ],
        [
            KeyboardButton(text='Б. Умный в гору не пойдет, умный гору обойдет')
        ],
        [
            KeyboardButton(text='В. Без труда не выловишь и рыбку из пруда')
        ],
        [
            KeyboardButton(text='Г. Лучшая защита - нападение')
        ],
    ],
    resize_keyboard=True
)

two_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Бродяга')
        ],
        [
            KeyboardButton(text='Б. Мыслитель')
        ],
        [
            KeyboardButton(text='В. Работяга')
        ],
        [
            KeyboardButton(text='Г. Охотник')
        ],
    ],
    resize_keyboard=True
)

three_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Оставаться здоровым и сильным')
        ],
        [
            KeyboardButton(text='Б. Познать себя и мир вокруг')
        ],
        [
            KeyboardButton(text='В. Приключения и свободу')
        ],
        [
            KeyboardButton(text='Г. Найти свое призвание')
        ],
    ],
    resize_keyboard=True
)

four_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Я легко справляюсь с трудностями')
        ],
        [
            KeyboardButton(text='Б. Я часто думаю о переселении души после смерти')
        ],
        [
            KeyboardButton(text='В. Я умею хранить секреты')
        ],
        [
            KeyboardButton(text='Г. Я трудоголик')
        ],
    ],
    resize_keyboard=True
)

five_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Лидерство ')
        ],
        [
            KeyboardButton(text='Б. Контроль')
        ],
        [
            KeyboardButton(text='В. Порядок и уюты')
        ],
        [
            KeyboardButton(text='Г. Приключения')
        ],
    ],
    resize_keyboard=True
)

six_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Изменений')
        ],
        [
            KeyboardButton(text='Б. Сложной работы')
        ],
        [
            KeyboardButton(text='В. Разоблачения')
        ],
        [
            KeyboardButton(text='Г. Конкуренции')
        ],
    ],
    resize_keyboard=True
)

seven_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Обидчивость')
        ],
        [
            KeyboardButton(text='Б. Лень')
        ],
        [
            KeyboardButton(text='В. Щедрость')
        ],
        [
            KeyboardButton(text='Г. Агрессивность')
        ],
    ],
    resize_keyboard=True
)

eight_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Мяса')
        ],
        [
            KeyboardButton(text='Б. Рыбы')
        ],
        [
            KeyboardButton(text='В. Круп')
        ],
        [
            KeyboardButton(text='Г. Деликатесов')
        ],
    ],
    resize_keyboard=True
)

nine_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Жить яркой и насыщенной жизнью')
        ],
        [
            KeyboardButton(text='Б. Помогать другим и делать добро')
        ],
        [
            KeyboardButton(text='В. Преодолеть все препятствия на пути к успеху')
        ],
        [
            KeyboardButton(text='Г. Стать лидером и основателем')
        ],
    ],
    resize_keyboard=True
)

ten_q_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='А. Сила воли')
        ],
        [
            KeyboardButton(text='Б. Общительность')
        ],
        [
            KeyboardButton(text='В. Стрессоустойчивость ')
        ],
        [
            KeyboardButton(text='Г. Бескорыстие')
        ],
    ],
    resize_keyboard=True
)

group_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ДА'),
            KeyboardButton(text='НЕТ'),
        ]
    ],
    resize_keyboard=True
)

finaly_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ЭТО БУДЕТ ЛЕ-ГЕН-ДАРНО ')
        ]
    ],
    resize_keyboard=True
)
