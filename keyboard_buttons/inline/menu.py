from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Namuna inline
menu1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔙 ORQAGA QAYTISH", callback_data="orqaga_qaytish"),
        ]
    ]
)
