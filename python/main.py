import asyncio
import io
import os
import time

from opentele.exception import TDesktopUnauthorized
from opentele.td import TDesktop, API
from opentele.tl import telethon
from telethon.errors import FloodWaitError

from python.properties import read_files

files = read_files()

from python.checkers import *

error_count = 0
start = time.time()
client: telethon.TelegramClient = None
client_path: str
bad_accounts_lines = []

bad_accounts: io.TextIOWrapper
fast: io.TextIOWrapper
slow: io.TextIOWrapper
trash: io.TextIOWrapper

is_end = False


def get_sub_paths(path):
    names = list(list(os.walk(path))[0])[1]
    paths = []

    for n in names:
        paths.append(path + n)

    return paths


def remove_session():
    os.remove(sys.path[1] + "\\python\\" + sessionName)


def no_accounts():
    global is_end
    print("No good accounts left")
    try:
        remove_session()
    except:
        pass

    is_end = True


def get_first_good_path(paths):
    for p in paths:
        if not bad_accounts_lines.__contains__(p):
            return p

    no_accounts()


async def update_client(tdata_path):
    global client_path, client
    client_path = tdata_path
    tdesk = TDesktop(basePath=tdata_path)
    api = API.TelegramIOS.Generate()

    client = await tdesk.ToTelethon(session=sessionName, api=api, password="1090ak")


async def goto_next_client(paths):
    global bad_accounts_lines, client

    if client is not None:
        try:
            await client.disconnect()
        except:
            pass

        os.remove(sys.path[1] + "\\python\\" + sessionName)
        bad_accounts.write(client_path + "\n")
        bad_accounts_lines.append(client_path)

    new = get_first_good_path(paths)

    if new is None:
        no_accounts()
        return

    print("Enabling client:\n" + new)

    try:
        await update_client(new)
        await client.start()
    except TDesktopUnauthorized:
        print("Bad account passed")
        client = None
        bad_accounts.write(client_path + "\n")
        bad_accounts_lines.append(client_path)
        await goto_next_client(paths)


async def main():
    global error_count, start, client, client_path, bad_accounts, bad_accounts_lines, fast, slow, trash

    path = sys.path[1] + "\\output\\"
    ext = ".txt"

    fast_path = path + FAST + ext
    slow_path = path + SLOW + ext
    trash_path = path + TRASH + ext
    error_path = path + "error.txt"

    try:
        os.remove(fast_path)
        os.remove(slow_path)
        os.remove(trash_path)
    except FileNotFoundError:
        print("Output files deleted. DO NOT DELETE THEM THE NEXT TIME !!!")
    finally:
        print('Files prepared')

    accounts_dir_path = sys.path[1] + "\\accounts\\"
    accounts_paths = get_sub_paths(accounts_dir_path)

    fast = open(fast_path, 'a')
    slow = open(slow_path, 'a')
    trash = open(trash_path, 'a')
    error = open(error_path, 'a')

    bad_accounts = open(accounts_dir_path + "\\bad_accounts_paths.txt", "r+")
    bad_accounts_lines = bad_accounts.readlines()

    for i in range(len(bad_accounts_lines)):
        bad_accounts_lines[i] = bad_accounts_lines[i].replace("\n", "")

    await goto_next_client(accounts_paths)

    try:
        count = 0
        found = 0
        files_amount = files.__sizeof__()
        error_count = 0
        one_account_chats_counter = 0

        for chat in files:
            if is_end:
                break
            try:
                if one_account_chats_counter >= chatsPerAccount:
                    print("Disabling client:\n" + client_path)
                    one_account_chats_counter = 0
                    await goto_next_client(accounts_paths)

                found += 1
                count += 1
                speed = await get_speed(client, chat)
                is_suitable_by_entity = await check_entity(client, chat)

                if speed == TRASH or not is_suitable_by_entity:
                    trash.write(chat)
                    found -= 1
                elif speed == SLOW:
                    slow.write(chat)
                else:
                    fast.write(chat)
            except FloodWaitError or TDesktopUnauthorized:
                await goto_next_client(accounts_paths)
            except:
                error.write(chat)
                print("error: " + chat)
                error_count += 1
            finally:
                one_account_chats_counter += 1
                if count % 25 == 0:
                    print(
                        '\n' +
                        str(count) +
                        ' CHATS PROCEED (' + str((count / files_amount) * 100) + '%) ' + str(found) + ' found\n' +
                        ' TIME: ' + str(time.time() - start)
                    )

    finally:
        try:
            await client.disconnect()
        except:
            pass

        fast.write('\n')
        slow.write('\n')
        trash.write('\n')

        print("errors: " + str(error_count))
        print("total time: " + str(time.time() - start))

        input("Press any key to continue")


asyncio.run(main())
