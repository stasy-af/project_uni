from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from our_words import words

router = Router()



@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, тебе нужна помощь с пониманием современных слэнговых слов? Я с удовольствием помогу тебе. Заинтересовало слово "скуф" в моем названии? Напиши мне его чтобы узнать его значение. Если тебе нужен полный список слов, которые я знаю, напиши /all_words')


@router.message(F.text[0] != '/')
async def resque_word(message: Message):
    request_word=message.text.lower()
    ans_was=0
    maybe_words=''
    for stroka in words:
        if request_word==stroka[0]:
            await message.answer(stroka[1])
            ans_was=1
            
    if ans_was == 0:
        for stroka in words:
            if all(char in stroka[0] for char in request_word ) and len(request_word)>=2 :
                maybe_words+=stroka[0]+', '
        
        if len(maybe_words)>0:
            await message.answer('Возможно ты имел в виду что-то из этого? (Если не нашел свое слово - отправляй сюда @megumiwaa и я его рассмотрю.)')
            await message.answer(maybe_words[:-2])
        else:
            await message.answer('Я не знаю такого слова 😭. Если ты уверен, что оно существует - отправляй сюда @megumiwaa и я его рассмотрю.')
    
    

            
@router.message(F.text == '/all_words')
async def resque_word(message: Message):
    all_words=""
    for stroka in words:
        all_words=all_words+stroka[0]+", "
    await message.answer(all_words[0:-2])
        