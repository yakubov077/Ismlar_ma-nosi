import time

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message

# Ushbu kodda Telegram botda spam yoki juda tez-tez yuborilayotgan xabarlarni cheklash maqsadida 
# foydalanuvchiga nisbatan "throttling" (tezlikni kamaytirish) tizimi amalga oshirilgan.

# BaseMiddleware: aiogram kutubxonasidagi asosiy middleware sinfi bo'lib, u botning 
# o'rnatilgan "vositachilik" sinflari bilan ishlashiga imkon beradi.

# Middleware — bu web dasturlar, xususan, Django kabi frameworklarda request (so'rov) va response 
# (javob) jarayonlarini boshqarish uchun ishlatiladigan qatlam yoki moduldir. Django'da middleware'lar 
# HTTP so'rovlari va javoblarini filtrlash yoki o'zgartirish uchun ishlatiladi, bu orqali dastur ishlashini 
# yanada optimallashtirish va xavfsizlikni ta'minlash mumkin.

class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, slow_mode_delay=0.5):
        # slow_mode_delay: Bu qiymat orqali so'rovlar orasidagi 
        # minimal vaqt oralig'i belgilanadi. Default qiymat sifatida 0.5 soniya berilgan.
        self.user_timeouts = {}
        # self.user_timeouts: Bu lug'at (dictionary) har bir foydalanuvchining so'nggi so'rov vaqti saqlanishi uchun ishlatiladi.
        self.slow_mode_delay = slow_mode_delay
        super(ThrottlingMiddleware, self).__init__()

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = time.time()
        
        # Ushbu foydalanuvchining so'nggi so'rovi bo'yicha yozuv mavjudligini tekshirish
        last_request_time = self.user_timeouts.get(user_id, 0)
        if current_time - last_request_time < self.slow_mode_delay:
            # Agar so'rovlar juda tez-tez bo'lsa, sekin rejimni yoqish
            await event.reply("Juda ko'p so'rov! Biroz kuting.")
            return
        
        else:
            # Oxirgi so'rovning vaqtini yangilash
            self.user_timeouts[user_id] = current_time
            # Event ni handlerga o'tkazish
            return await handler(event, data)