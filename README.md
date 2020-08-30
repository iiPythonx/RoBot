# RoBot
# The most basic bot in existance for Roblox.
---

RoBot is a bot that uses a Roblox client and can perform actions automatically.
It uses `pygetwindow` to focus on Roblox and send keypresses to it.

Since it only uses keypresses, RoBot does **not** require administrator privileges or
require you to enter credentials.

---

### Installation
- Ensure that you have downloaded (and installed!) Python 3.6 or later (3.8+ recommended).
  - **This includes adding it to your path!**
- Download the source code via the `Code` and `Download ZIP` buttons.
- Locate the zip folder you downloaded and extract it.
- Install the dependencies by opening a terminal in the extracted directory and executing `pip install -r requirements.txt`.

### Using the Bot
- Open a Roblox game window
- Double click (or launch by terminal) the `main.py` file.
  - It could take 5 - 15 seconds to start up.
  - Clicking on the graph that opens will move the bot to a certain coordinate.

You can also provide some options to the bot.
To do this, make sure you're launching the bot via terminal.

To add an option, call the bot like so: `python main.py [options]`

**Available Options:**
  - `-q` and `--quiet`, disables chat output.
---

### API Example
Since this is a keypress-only bot, RoBot has provided a folder containing
functions related to movement, chatting, window management, and keystrokes.

The API is contained in the `/api/` directory.
Quick example:

```
from time import sleep
from api.keybinds import Chat

from api.windows import WindowManager
from api.user import leaveGame, resetChar

# Focuses on the current roblox instance
# Raises errors.NoRobloxInstance
HANDLER = WindowManager()
HANDLER.focusROBLOX()

sleep(.1) # To account for the window delay

Chat("Hello, world.")

sleep(5)

leaveGame() # Leave the current game
```

---

Last updated: **8/30/2020**.
