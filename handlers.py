from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from our_words import words

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, тебе нужна помощь с пониманием современных слэнговых слов? Я с удовольствием помогу тебе. Заинтересовало слово "скуф" в моем названии? Напиши мне его чтобы узнать его значение. Если тебе нужен полный список слов, которые я знаю, напиши /all_words')

@router.message(F.text != '/start')
async def resque_word(message: Message):
    request_word=message.text.lower()
    ans_was=0
    for stroka in words:
        if stroka[0]==request_word:
            await message.answer(stroka[1])
            ans_was=1
            
    if ans_was == 0:
        await message.answer('К сожалению, даже я не знаю этого слова😭. Пожалуйста проверь правильно ли ты его написал. Если всё верно отправляй слово, которое не понимаешь, сюда *******, и я рассмотрю его.')
            
        
            
