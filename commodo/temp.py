from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

button = InlineKeyboardButton(text="Button Text", web_app=WebAppInfo(url="https://www.example.com type="default")
keyboard = InlineKeyboardMarkup().add(button)
