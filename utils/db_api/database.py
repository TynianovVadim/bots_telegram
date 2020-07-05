from gino import Gino
from gino.schema import GinoSchemaVisitor
from aiogram import types, Bot
from sqlalchemy import (Column, Integer, BigInteger, Boolean, TIMESTAMP, String, Sequence, JSON)
from sqlalchemy import sql

from data.config import DB_PASS, DB_USER, HOST

db = Gino()


class User(db.Model):
    __tablename__ = "users"
    query: sql.Select

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))
    referral = Column(BigInteger)

    def __repr__(self):
        return "<User(id={}, fullname={}, username={})>".format(self.id, self.full_name, self.username)


class Item(db.Model):
    __tablename__ = "items"
    query: sql.Select

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    name = Column(String(200))
    photo = Column(String(250))
    price = Column(Integer)  # цена в копейках

    def __repr__(self):
        return "<Item(id={}, name={}, price={})>".format(self.id, self.name, self.price)


class Purchase(db.Model):
    __tablename__ = "purchases"
    query: sql.Select

    id = Column(Integer, Sequence("user_id_seq"), primary_key=True)
    buyer = Column(BigInteger)
    item_id = Column(Integer)
    amount = Column(Integer)  # цена в копейках
    quantity = Column(Integer)
    purchase_time = Column(TIMESTAMP)
    shopping_address = JSON
    phone_number = Column(String(50))
    email = Column(String(250))
    receiver = Column(String(100))
    successful = Column(Boolean, default=False)


class DBCommands:


    async def get_user(self, user_id) -> User:
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user


    async def add_new_user(self, referral=None) -> User:
        user = types.User.get_current()
        old_user = self.get_user(user.id)
        if old_user:
            return old_user

        new_user = User()
        new_user.user_id = user.id
        new_user.full_name = user.full_name
        new_user.user_id = user.username

        if referral:
            new_user.referral = int(referral)

        await new_user.create()
        return new_user

    async def set_languge(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()

    async def count_user(self):
        total = await db.func.count(User.id).gino.scalar()
        return total

    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current().id

        user = await User.query.where(User.user_id == user_id).gino.first()
        referrals = await User.query.where(User.referral == user.id).gino.all()

        return ",".join(
            f"{num+1}. {(await bot.get_chat(ref.user_id)).get_mention(as_html=True)}"
            for num, ref in enumerate(referrals)
        )

    async def show_items(self):
        items = Item.query.gino.all()
        return items


async def create_db():
    await db.set_bind(f'postgresql://{DB_USER}:{DB_PASS}@{HOST}/gino')

    #  создание таблицы
    db.gino: GinoSchemaVisitor
    await db.gino.drop_all()
    await db.gino.create_all()
