import asyncio
import datetime
import json
import sqlite3
from contextlib import suppress
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hlink
from aiogram.dispatcher.filters import Text
from data_base import pg_db
from main import bot, dp
from keyboards import user_kb
from aiogram.utils.markdown import hbold, hlink
#from scrapingfile import dollar_exchange_rate, euro_exchange_rate


db = pg_db.DataBase('exchange_rate.db')

connect = sqlite3.connect('exchange_rate.db')
cursor = connect.cursor()


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}! Добро пожаловать в DX_exchange \n'
                         f'С помощью этого бота вы сможете узнать о самых выгодных курсах валют',
                         reply_markup=user_kb.inline_kb)
    try:
        await db.add_users(message.chat.id, message.chat.first_name)
    except Exception as e:
        pass



@dp.message_handler(Text(equals="USD"))
async def get_usd_currency(message: types.Message):

    with open('scrapingfile\dollar_exchange_rate.json', encoding='utf-8') as file:
        usd_currency_dict = json.load(file)

    list1 = usd_currency_dict.get('currency_purchase')[-5:]
    list2 = usd_currency_dict.get('currency_sale')[:5]

    result1 = "\n".join([i.replace("\n", " ").ljust(20) + "  " for i in list1])
    result2 = "\n".join([i.replace("\n", " ").ljust(20) + "  " for i in list2])
    await message.answer(f'<b>ПОКУПКА:</b>\n\n<strong>{result1}</strong>\n\n\n'
                         f'<b>ПРОДАЖА:</b>\n\n<strong>{result2}</strong>\n', parse_mode='HTML')
                         #f'<a>{usd_currency_dict.get("currency_url")}</a>', parse_mode='HTML')


@dp.message_handler(Text(equals="EUR"))
async def get_eur_currency(message: types.Message):

    with open('scrapingfile\euro_exchange_rate.json', encoding='utf-8') as file:
        eur_currency_dict = json.load(file)

    list1 = eur_currency_dict.get('currency_purchase')[-5:]
    list2 = eur_currency_dict.get('currency_sale')[:5]

    result1 = "\n".join([i.replace("\n", " ").ljust(20) + "  " for i in list1])
    result2 = "\n".join([i.replace("\n", " ").ljust(20) + "  " for i in list2])
    await message.answer(f'<b>ПОКУПКА:</b>\n\n<strong>{result1}</strong>\n\n\n'
                         f'<b>ПРОДАЖА:</b>\n\n<strong>{result2}</strong>\n', parse_mode='HTML')
                         #f'<a>{eur_currency_dict.get("currency_url")}</a>', parse_mode='HTML')
