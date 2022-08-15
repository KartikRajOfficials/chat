import sys

api_id = 9461614
api_hash = '959f136e17d280230d1bb98121af74fd'
sessionName = 'autoslave.session'

phone = '+79653995169'

trashBound = 10
slowBound = 50
membersBound = 200
chatsPerAccount = 70
accuracyLimit = 300

FAST = 'fast'
SLOW = 'slow'
TRASH = 'trash'


def read_settings():
    try:
        path = normalize_path(sys.path[1] + "\\properties\\settings.txt")
        f = open(path)
        lines = f.readlines()
        global trashBound, slowBound, membersBound, chatsPerAccount, accuracyLimit
        trashBound = int(lines[0].replace("\n", ""))
        slowBound = int(lines[1].replace("\n", ""))
        membersBound = int(lines[2].replace("\n", ""))
        chatsPerAccount = int(lines[3].replace("\n", ""))
        accuracyLimit = int(lines[4].replace("\n", ""))
    except:
        print("Settings are absent or not properly formatted. Using default settings")
        quit()


def read_input_chats():
    f = open(normalize_path(sys.path[1] + '\\properties\\input.txt'))
    return f.readlines()


def read_files():
    read_settings()
    return read_input_chats()


def normalize_path(path: str):
    res = path.replace("\\dist\\main\\lib-dynload", "")
    return res
