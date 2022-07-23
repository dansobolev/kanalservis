import datetime

from sqlalchemy import (
    Column, Integer, TIMESTAMP, Date, Boolean
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column('id', Integer, unique=True, primary_key=True)
    created_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow,
    )
    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )

    def __repr__(self):
        return f'{self.__class__.__name__}'


class EntityInformation(BaseModel):
    __tablename__ = 'entities_information'

    order_number = Column('order_number', Integer, doc='Номер заказа')
    price_dollar = Column('price_dollar', Integer, doc='Стоимость в долларах')
    delivery_time = Column('delivery_time', Date, doc='Срок поставки')
    price_rub = Column('price_rub', Integer, doc='Стоимость в рублях')
    notification_send = Column('notification_send', Boolean,
                               default=False, doc='Статус отправленного сообщение по истечению срока поставки')
