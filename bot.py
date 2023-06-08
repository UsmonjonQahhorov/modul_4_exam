import os

import aiogram
from aiogram import Bot, types, Dispatcher, executor
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN = os.environ["TOKEN"]
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='start')
async def main_menu(message: types.Message, state: FSMContext ):
    await message.answer(f"Assalomu alaykum {message.from_user.username}, textni yozing👉")
    await state.set_state('text')


@dp.message_handler(state='text')
async def delete_message_with_five_vowels(message: types.Message, state: FSMContext):
    vowels = 'aeiouAEIOU'
    vowel_count = sum([1 for letter in message.text if letter in vowels])
    if vowel_count >= 5:
        await message.delete()
        await message.answer("Textdagi unli xarflar soni 5 tadan ortiq\n"
                             "qaytadan kiriting👉")
        await state.set_state('text')
    else:
        await state.set_state('text')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
