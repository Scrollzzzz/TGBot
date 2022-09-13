from create import dp
import markups as nav
import handlers.client as cl

import json

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State


currencies = (
    'USD', 'EUR', 'RUB', 'JPY', 'AUD',
    'GBP', 'CAD', 'CHF', 'CNY', 'SEK',
    'NZD', 'KRW', 'TRY', 'INR', 'MXN'
)


class FSM(StatesGroup):
    currency = State()
    original_type = State()
    target_type = State()


@dp.message_handler(Text(equals='Курс валют'))
async def currency(message: types.Message):
    await FSM.currency.set()
    await message.answer('Выберите валюту', reply_markup=nav.curMenu)


@dp.message_handler(Text(equals=currencies), state=FSM.currency)
async def original_currency(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['requestID'] = '2'
        data['original_currency'] = message.text

    await FSM.next()
    await message.answer('Выберите целевую валюту', reply_markup=nav.curMenu)


@dp.message_handler(Text(equals=currencies), state=FSM.original_type)
async def target_currency(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['target_currency'] = message.text

    await FSM.next()
    await message.answer('Введите количество', reply_markup=nav.backMenu)


@dp.message_handler(state=FSM.target_type)
async def amount(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['amount'] = float(message.text)

    async with state.proxy() as data:
        request = json.dumps(data.as_dict())
    response = cl.client_program(request)

    await state.finish()
    answer = f'{data["original_currency"]} {data["amount"]} ⇌ {round(float(response), 3)} {data["target_currency"]}'
    await message.answer(answer, reply_markup=nav.mainMenu)
