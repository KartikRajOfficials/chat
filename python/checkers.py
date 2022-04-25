from python.properties import *
from python.time_utils import *
from telethon.tl.functions.channels import GetFullChannelRequest


def is_activity_enough(messages, chat_name):
    messages.reverse()

    first_date = datetime.datetime.now(tz=datetime.timezone.utc)
    first_time = get_hours(first_date)
    senders = set()

    amount = len(messages)
    for m in messages:
        cur = get_hours(m.date)
        delta = first_time - cur
        if delta > 24:
            amount -= 1
            continue

        senders.add(str(m.from_id))
        if len(senders) >= sendersBound:
            break

    if len(senders) < sendersBound:
        print(chat_name + " - trash(" + len(senders).__str__() + " senders)")
        return TRASH

    amount /= 24

    if amount <= trashBound:
        print(chat_name + " - trash(" + amount.__str__() + " per hour)")
        return TRASH
    elif amount <= slowBound:
        print(chat_name + " - slow(" + amount.__str__() + " per hour)")
        return SLOW
    else:
        print(chat_name + " - fast(" + amount.__str__() + " per hour)")
        return FAST


def is_group(entity, chat_name):
    if entity.broadcast:
        print(chat_name + ': chat is a channel (-)')
    return not entity.broadcast


async def is_subscribers_suitable(client, entity, chat_name):
    channel_full_info = await client(GetFullChannelRequest(entity))
    members = channel_full_info.full_chat.participants_count

    if members < membersBound:
        print(chat_name + ': too small amount of members (-)')

    return members >= membersBound


async def check_entity(client, chat_tag):
    entity = await client.get_entity(chat_tag)
    is_group_result = is_group(entity, chat_tag)
    subscribers = await is_subscribers_suitable(client, entity, chat_tag)
    return is_group_result and subscribers


async def get_speed(client, chat_tag):
    messages = await client.get_messages(entity=chat_tag, limit=1205)

    activity = is_activity_enough(messages, chat_tag)
    return activity