import sys

api_id = 9461614
api_hash = '959f136e17d280230d1bb98121af74fd'
sessionName = 'autoslave.session'

phone = '+79653995169'

trashBound = 10
slowBound = 50
sendersBound = 10
membersBound = 200
chatsPerAccount = 70

FAST = 'fast'
SLOW = 'slow'
TRASH = 'trash'


def read_settings():
    # try:
        f = open(sys.path[1] + "\\properties\\settings.txt")
        lines = f.readlines()
        global trashBound, slowBound, membersBound, sendersBound, chatsPerAccount
        trashBound = int(lines[0].replace("\n", ""))
        slowBound = int(lines[1].replace("\n", ""))
        sendersBound = int(lines[2].replace("\n", ""))
        membersBound = int(lines[3].replace("\n", ""))
        chatsPerAccount = int(lines[4].replace("\n", ""))
    # except:
    #     print("Settings are absent or not properly formatted. Using default settings")


def read_input_chats():
    f = open(sys.path[1] + '\\properties\\input.txt')
    return f.readlines()


def read_files():
    read_settings()
    return read_input_chats()
