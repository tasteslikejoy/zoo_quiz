from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    one_name_answer = State()
    two_name_answer = State()
    three_name_answer = State()
    four_name_answer = State()
    five_name_answer = State()
    six_name_answer = State()
    seven_name_answer = State()
    eight_name_answer = State()
    nine_name_answer = State()
    ten_name_answer = State()
    yes_or_no_name_answer = State()

class FormFinaly(StatesGroup):
    one_name_finaly_answer = State()
    two_name_finaly_answer = State()
    three_name_finaly_answer = State()
    four_name_finaly_answer = State()