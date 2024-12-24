from aiogram.types import Message
from loader import dp,db
from aiogram.filters import CommandStart
from keyboard_buttons.default.button import button_1

@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id) #foydalanuvchi bazaga qo'shildi
        await message.answer(text=f"""Salom <b>{full_name}</b> botimizga hush kelibsiz !\n
<b>📖 ISMLAR MA'NOSI</b> - Ismingiz ma'nosini bilish uchun bosing!\n
<b>📄 QO'LLANMA</b> - Bot haqida ma'lumot olish uchun bosing!""",parse_mode='html',reply_markup=button_1)
    except:
        await message.answer(text=f"""Salom <b>{full_name}</b> botimizga hush kelibsiz !\n
<b>📖 ISMLAR MA'NOSI</b> - Ismingiz ma'nosini bilish uchun bosing!\n
<b>📄 QO'LLANMA</b> - Bot haqida ma'lumot olish uchun bosing!""",parse_mode='html',reply_markup=button_1)
