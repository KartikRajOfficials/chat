import datetime
from telethon.tl.custom import Message


def get_minutes(message: Message):
    return message.date.hour * 60 + message.date.minute


def get_hours(dt):
    return timestamp(dt) / 3600000


def timestamp(dt):
    return dt.replace(tzinfo=datetime.timezone.utc).timestamp() * 1000
