from loader import dp
from aiogram.types import Message, ReplyKeyboardRemove,CallbackQuery
from aiogram import F
from aiogram.fsm.context import FSMContext
from ism_manosi import ism_manosi_funksiyasi
from states.help_stt import Baza
from keyboard_buttons.default.button import button_2, button_1

@dp.message(F.text == "📖 ISMLAR MA'NOSI")
async def ismmanosi_start(message: Message, state: FSMContext):
    text = "<b>📝 Manosi bilmoqchi bo'lgan ism yozing\n🔹 Masalan:</b> Akbar\n"
    await message.answer(text,reply_markup=ReplyKeyboardRemove(),parse_mode='html')
    await state.set_state(Baza.ismlar)

@dp.message(F.text,Baza.ismlar)
async def ismmanosi_result(message: Message, state: FSMContext):
    ism = message.text
    ism = ism.replace("'", "‘")  # Matnni to'g'irlash
    manosi = ism_manosi_funksiyasi(ism=ism)  # Ism ma'nosini olish

    if manosi:  
        text = f"✨ {ism} ismining ma'nosi:\n{manosi}"
    else: 
        text = "<b>Afsuski topilmadi ✖️</b>"
    await message.answer(text,parse_mode='html',reply_markup=button_2)
    await state.clear()

@dp.message(F.text == "📄 QO'LLANMA")
async def ismmanosi_start(message: Message):
    text = """<b>📄 QO'LLANMA</b>\n\nIsmingiz ma'nosini bilish uchun menyudan <b>📖 ISMLAR MA'NOSI</b> degan tugmasini tanlang va xoxlagan ismingizni yozib yuboring. Bot esa tezda so'ralgan ism ma'nosini sizga yuboradi!\n\nAgar yordamga muhtoj bo'lsangiz, biz bilan bog'laning yoki /xabar berish tugmasini bosing. ❗️"""
    await message.answer(text,parse_mode='html')

@dp.message(F.text == "🔙 ORQAGA QAYTISH")
async def ismmanosi_start(message: Message):
    text = "<b>🏠 Siz bosh menyudasiz</b>"
    await message.answer(text,parse_mode='html',reply_markup=button_1)
    await message.delete()