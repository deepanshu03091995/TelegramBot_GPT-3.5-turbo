import logging
from aiogram import Bot, Dispatcher, types,executor
from dotenv import load_dotenv

import os
load_dotenv()


API_TOKEN=os.environ["TOKEN"]

logging.basicConfig(level=logging.INFO)
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` ar `/help` command
    """
    
    await message.reply("Hi\nI am EchoBot\n Powered by aiogram")
    
@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """
    
    await message.answer(message.text)    
    
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)    
    
