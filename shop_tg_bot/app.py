import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

from shop_tg_bot import config
from shop_tg_bot.bot_settings import TELEGRAM_BOT_TOKEN

bot = Bot(TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply(
        "Привет! Это бот для получения списка товаров. Нажми на кнопку, чтобы получить список."
    )


@dp.message_handler(commands=["get_categories"])
async def get_categories(message: types.Message):
    answer = ""
    for word in config.categories_list(is_list=True):
        answer += word + "," + "\n"
    await message.reply(answer)


@dp.message_handler(commands=["get_products"])
async def get_categories(message: types.Message):
    for line in config.products_list():
        answer = ""
        answer += "Название" + " " + str(line.get("name")) + "\n"
        answer += "Категория" + " " + str(line.get("category")) + "\n"
        answer += str(line.get("description")) + "\n"
        answer += str(line.get("sell_price")) + "\n"
        answer += "Количество" + " " + str(line.get("quantity")) + "\n"
        await message.reply(answer)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
