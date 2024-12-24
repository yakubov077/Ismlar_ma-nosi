from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#help commands
@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("""Salom! Ushbu botdan foydalanish bo'yicha yordam:\n
▪️ /start - Botni ishga tushirish va menyuni ko'rish.\n
▪️ /about - Bot haqida to'liq ma'lumot.\n
▪️ /xabar - Adminga xabar yuborish uchun.\n
Ism ma'nosini bilish uchun ismni yozib yuboring, va bot sizga uning ma'nosini chiqarib beradi.\n
Agar qo'shimcha yordam kerak bo'lsa yoki muammo yuzaga kelsa, /xabar orqali admin bilan bog'lanishingiz mumkin.""")
