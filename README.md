# RoBot
# Just a bot for Roblox clients
---

RoBot is a utility bot that uses a Roblox client and can perform actions automatically.
It uses `pygetwindow` to focus on Roblox and send keypresses to it.

It also has a neat little interface made using `pygame`, other than those it has no dependencies.

---
### Security Notice
Since it only uses keypresses, RoBot does **not** require administrator privileges or
require you to enter credentials.

---

### Installation
- Ensure that you have downloaded (and installed!) Python 3.6 or later (3.8+ recommended).
  - **This includes adding it to your path!**
- Ensure that you have the latest version of git installed.
- Clone the repository with `git clone https://github.com/ii-Python/RoBot`.
- Enter the newly created directory with `cd RoBot`.
- Install the dependencies via pip: `python -m pip install -r requirements.txt`.

### Usage
**Before attempting to start the bot, make sure you have a window open! It will raise `errors.NoRobloxInstance` otherwise.**

- Join a new Roblox game and wait for it to load completely.
- Double click (or launch by terminal) the `main.py` file.
  - Please note this could take a few seconds to initialize.
- Once started, you can use the GUI that shows up on your screen.

You can also provide some options to the bot.
To do this, make sure you're launching the bot via terminal.

To add an option, call the bot like so: `python main.py [options]`

**Available Options:**
  - `-q` *or* `--quiet`, disables chat output.
---

### API
Since this is a keypress-only bot, RoBot has provided a folder containing
functions related to movement, chatting, window management, and keystrokes.

The API is contained in the `api` directory.
An example application might look like the following:

```
from time import sleep
from api.keybinds import Chat

from api.windows import WindowManager
from api.user import leaveGame, resetChar

# Focuses on the current roblox instance
# Raises `errors.NoRobloxInstance` if one wasn't located
HANDLER = WindowManager()
HANDLER.focusROBLOX()

sleep(.1)  # This will account for the delay while switching windows

# Execute anything you want here
Chat("Hello, world.")

sleep(5)

leaveGame()  # Leaves the current game
```

---

Last updated: **11/3/2020**.
