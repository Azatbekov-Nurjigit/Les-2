
import logging
from aiogram.utils import executor
from coin import  dp
from handlers import client, callback, eztra



client.register_handler_client(dp)
callback.register_handler_callback(dp)
eztra.register_handler_ezta(dp)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)



# 1. К викторинам, которые уже существуют,
# добавить
# Callback (Очередность вопросов с помощью
# кнопок).
# ответов должно быть по 3 продолжения
# 2. Закреплять сообщение при команде "!pin"
# , только
# если это будет ответом на сообщение.
# 3. Если сообщение начинается на game, пусть бот
# отправляет рандомный анимированный эмодзи из
# ниже перечисленных:
# [ , , ⚽️ , , , ]


# Создать команду dice, при вызове
# которой бот кинет 2 игральной кости
# для бота и для игрока. Затем бот
# должен определить победителя.










