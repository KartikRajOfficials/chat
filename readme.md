#Autoslave

Sorts telegram chats to *TRASH*, *SLOW* and *FAST* Using such criteria as:
- Average number of messages that should appear in chat per hour
- Number of users that should be active in chat within one **DAY**
- Minimal amount of members in chat.
##Usage
* Place your list of chats in `input.txt` file.
* Place your settings **IN CORRECT ORDER** into `settings.txt` file.
* Place your tdata folders into accounts folder.
Each number should be written on a new line.
    - trashBound = 10 by default. If a chat has `trashBound` or less
    messages per hour, it will be determined as `TRASH`
    - slowBound = 50 by default. If chat's messages per one hour is
    between `trashBound` and `slowBound`, the chat will be determined
    as `SLOW`. If this value is bigger than `slowBound`, the chat
    will be determined as `FAST`
    - sendersBound = 10 by default. Reflects minimal amount of users,
    that should be active within 24 hours. If this value is not reached,
    the chat is determined as `TRASH`
    - membersBound = 200 by default. The minimal amount of chat members.
    If this value is not reached, the chat is determined as `TRASH`
    - chatsPerAccount = 70 by default. Represents number of chats that
    should be processed by each account. **Do not make this parameter bigger than 98.**
    In other case your account will probably get FloodWait.
* Launch `main` function
* Enter your phone number
* Enter code that you received to telegram
* Enter password if you use 2FA.
* Enjoy!
