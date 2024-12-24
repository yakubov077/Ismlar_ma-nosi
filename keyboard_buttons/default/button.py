from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove

button_1= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📖 ISMLAR MA'NOSI"),
            KeyboardButton(text="📄 QO'LLANMA"),
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Menudan birini tanlang"
)

button_2= ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔙 ORQAGA QAYTISH")
        ]
        
    ],
   resize_keyboard=True,
   input_field_placeholder="Orqaga qaytish"
)
