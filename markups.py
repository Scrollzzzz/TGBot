from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menuB = KeyboardButton('Главное меню')
weatherB = KeyboardButton('Погода')
currencyB = KeyboardButton('Курс валют')

mscB = KeyboardButton('Москва')
omskB = KeyboardButton('Омск')
spbB = KeyboardButton('Санкт-Петербург')
krskB = KeyboardButton('Красноярск')
nnB = KeyboardButton('Нижний Новгород')

usdB = KeyboardButton('USD')
eurB = KeyboardButton('EUR')
rubB = KeyboardButton('RUB')
jpyB = KeyboardButton('JPY')
gbpB = KeyboardButton('GBP')
audB = KeyboardButton('AUD')
cadB = KeyboardButton('CAD')
chfB = KeyboardButton('CHF')
cnyB = KeyboardButton('CNY')
sekB = KeyboardButton('SEK')
nzdB = KeyboardButton('NZD')
krwB = KeyboardButton('KRW')
tryB = KeyboardButton('TRY')
inrB = KeyboardButton('INR')
mxnB = KeyboardButton('MXN')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(weatherB, currencyB)
backMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(menuB)
cityMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(mscB, krskB, omskB, spbB, nnB).add(menuB)
curMenu = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5).add(usdB, eurB, rubB, jpyB, gbpB, audB, cadB, chfB,
                                                                     cnyB, sekB, nzdB, krwB, tryB, inrB, mxnB, menuB)
