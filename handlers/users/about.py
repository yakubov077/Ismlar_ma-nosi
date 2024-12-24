from aiogram.types import Message
from loader import dp
from aiogram.filters import Command

#about commands
@dp.message(Command("about"))
async def about_commands(message:Message):
    await message.answer("Bot haqida to'liq ma'lumot olish uchun <b>📄 QO'LLANMA</b> degan tugmani bosing !",parse_mode='html')

