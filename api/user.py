# Modules
from .keybinds import Hotkey

# Functions
def equipItem(slotNo):

    Hotkey(str(slotNo))
    
def leaveGame():

    Hotkey("[ESC]", .35)

    Hotkey("L", .1)

    Hotkey("[ENTER]", .35)

def resetChar():

    Hotkey("[ESC]", .35)

    Hotkey("R", .1)

    Hotkey("[ENTER]", .35)
