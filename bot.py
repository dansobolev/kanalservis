import telebot

from db.models import EntityInformation
from config import Config

bot = telebot.TeleBot(Config.TG_BOT_TOKEN)


def send_notification_delivery_time_msg(data: EntityInformation) -> None:
    bot.send_message(Config.TG_CHAT_ID,
                     f'У заказа номер {data.order_number} стоимостью {data.price_dollar}$ '
                     f'прошел срок доставки - {data.delivery_time}')
