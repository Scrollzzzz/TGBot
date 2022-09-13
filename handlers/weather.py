from create import dp
import markups as nav
import handlers.client as cl

import json

from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_datepicker import Datepicker


cities = {
    'Москва': 'Moscow',
    'Санкт-Петербург': 'St. Petersburg',
    'Омск': 'Omsk',
    'Нижний Новгород': 'Nizhny Novgorod',
    'Красноярск': 'Krasnoyarsk'
}


class FSM(StatesGroup):
    weather = State()
    city = State()


@dp.message_handler(Text(equals='Погода'))
async def weather(message: types.Message):
    await FSM.weather.set()
    await message.answer('Выберите город', reply_markup=nav.cityMenu)


@dp.message_handler(Text(equals=cities.keys()), state=FSM.weather)
async def city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['requestID'] = '1'
        data['city'] = cities[message.text]
    await FSM.next()

    datepicker = Datepicker(cl.get_datepicker_settings())
    markup = datepicker.start_calendar()

    await message.answer(message.text, reply_markup=nav.backMenu)
    await message.answer('Выберите дату', reply_markup=markup)


@dp.callback_query_handler(Datepicker.datepicker_callback.filter(), state=FSM.city)
async def _process_datepicker(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    datepicker = Datepicker(cl.get_datepicker_settings())
    date = await datepicker.process(callback_query, callback_data)
    if date:
        async with state.proxy() as data:
            data['date'] = date.strftime('%Y-%m-%d')

        async with state.proxy() as data:
            request = json.dumps(data.as_dict())
        response = cl.client_program(request)

        answer = f'Погода в {list(cities.keys())[list(cities.values()).index(data["city"])]}: {response}'
        await callback_query.message.answer(answer, reply_markup=nav.mainMenu)
        await state.finish()
    await callback_query.answer()
