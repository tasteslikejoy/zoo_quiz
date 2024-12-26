from datetime import datetime

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.future import select


DATABASE_URL = 'postgresql+asyncpg://postgres:212397@localhost:5433/zoo_bot'
engine = create_async_engine(DATABASE_URL, echo=True)


async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, unique=True, nullable=False)
    username = Column(String, nullable=True)

    answers = relationship('Answer', back_populates='user')
    answer_counts = relationship('AnswerCount', back_populates='user')

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship('User', back_populates='answers')

class AnswerCount(Base):
    __tablename__ = 'answer_counts'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    answer = Column(String(1), nullable=False)  # A, B, C, D
    count = Column(Integer, default=0)

    user = relationship('User', back_populates='answer_counts')

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def create_user(chat_id: int, username: str):
    async with async_session() as session:
        try:
            result = await session.execute(
                select(User).where(User.chat_id == chat_id)
            )
            existing_user = result.scalar_one_or_none()

            if existing_user:
                print(f"User already exists with ID: {existing_user.id}")  # Debugging line
                return existing_user.id

            new_user = User(chat_id=chat_id, username=username)  # Сохраняем chat_id и username
            session.add(new_user)
            await session.commit()
            await session.refresh(new_user)  # Обновляем объект, чтобы получить новый ID
            print(f"Created new user with ID: {new_user.id}")  # Debugging line
            return new_user.id

        except SQLAlchemyError as e:
            print(f"Error occurred while creating user: {e}")  # Логируем ошибку
            await session.rollback()  # Откатываем сессию в случае ошибки
            return None  # Или выбросьте исключение, в зависимости от вашей стратегии обработки ошибок


async def create_or_update_answer_count(user_id: int, answer: str, count):
    if user_id is None:
        raise ValueError("user_id cannot be None")

    # Убедитесь, что count является целым числом
    if isinstance(count, str):
        try:
            count = int(count)  # Пробуем преобразовать строку в целое число
        except ValueError:
            raise ValueError("count must be an integer")

    if not isinstance(count, int):
        raise ValueError("count must be an integer")

    async with async_session() as session:
        result = await session.execute(
            select(AnswerCount).where(AnswerCount.user_id == user_id, AnswerCount.answer == answer)
        )
        existing_count = result.scalar_one_or_none()

        if existing_count:
            # Убедитесь, что existing_count.count является целым числом
            if isinstance(existing_count.count, str):
                existing_count.count = int(existing_count.count)  # Преобразуем строку в целое число
            existing_count.count += count  # Увеличиваем на предоставленное значение
        else:
            new_count = AnswerCount(user_id=user_id, answer=answer, count=count)
            session.add(new_count)

        await session.commit()



async def get_answer_counts(user_id: int):
    async with async_session() as session:
        result = await session.execute(
            select(AnswerCount).where(AnswerCount.user_id == user_id)
        )
        return {row.answer: row.count for row in result.scalars().all()}
