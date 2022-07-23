import datetime

from db.models import EntityInformation
from db.database import db
from utils import convert_str_to_date_object
from bot import send_notification_delivery_time_msg

model_fields = [column.name
                for column in EntityInformation.__table__.columns
                if column.name not in ['created_at', 'updated_at']]


def update_entities_state(data: list) -> None:
    db_objects_list = []
    existed_entities_ids = [entity.order_number for entity in db.query(EntityInformation).all()]
    for entity in data:
        # new brand new object
        if int(entity[1]) not in existed_entities_ids:
            entity[3] = convert_str_to_date_object(entity[3])
            data_dict = {key: value for key, value in zip(model_fields, entity)}
            db_object = EntityInformation(**data_dict)
            db_objects_list.append(db_object)

        # object is changed
        else:
            db_object = db.query(EntityInformation)\
                .filter(EntityInformation.order_number == entity[1])\
                .first()
            for property_, value in zip(model_fields, entity):
                db_object.property_ = value

            existed_entities_ids.remove(db_object.order_number)

        # sending notification to telegram if delivery time is arrived
        if (datetime.datetime.now().date() - db_object.delivery_time) >= datetime.timedelta(days=1) and \
                not db_object.notification_send:
            send_notification_delivery_time_msg(db_object)
            db_object.notification_send = True

    # adding new items
    db.add_all(db_objects_list)
    # delete items that is not included in google sheet
    db.query(EntityInformation)\
        .filter(EntityInformation.order_number.in_(existed_entities_ids))\
        .delete()
    db.commit()
