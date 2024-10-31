from loader import dp
from aiogram.types import Message
from aiogram import F
from ism_manosi import ism_manosi_funksiyasi

@dp.message(F.text)
async def ismmanosi(message:Message):
    ism = message.text
    ism = ism.replace("'","‘")
    manosi = ism_manosi_funksiyasi(ism=ism)
    text = f"✨ {ism} ma'nosi :\n{manosi}"
    if manosi == False:
        text = "Afsuski topilmadi 😢"
    await message.answer(text)