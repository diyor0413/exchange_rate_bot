from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
inline_kb_usd = KeyboardButton('USD')
inline_kb_eur = KeyboardButton('EUR')

inline_kb.add(inline_kb_usd, inline_kb_eur)