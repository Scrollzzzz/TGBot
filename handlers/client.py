import config
from create import dp
import markups as nav

import socket

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram_datepicker import DatepickerSettings


def get_datepicker_settings():
    return DatepickerSettings()


def client_program(client_data):
    host = config.HOST
    port = config.PORT

    client_socket = socket.socket()
    client_socket.connect((host, port))

    client_socket.send(client_data.encode())
    data = client_socket.recv(1024).decode()

    client_socket.close()

    return data


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer('ok', reply_markup=nav.mainMenu)


@dp.message_handler(Text(equals='Главное меню'), state='*')
async def weather(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('ok', reply_markup=nav.mainMenu)
