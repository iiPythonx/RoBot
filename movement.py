# Modules
from random import choice
from keybinds import Hotkey

# Initialization
CURRENT_POS = (0, 0)

# Functions
def Move(direction):

    if direction == "FORWARD":

        Hotkey("W", 1.35)

    elif direction == "LEFT":

        Hotkey("A", 1.35)

    elif direction == "RIGHT":

        Hotkey("D", 1.35)

    elif direction == "BACKWARD":

        Hotkey("S", 1.35)

    elif direction == "UP":

        Hotkey(" ", .35)

def RandomMove():

    Move(choice(["FORWARD", "LEFT", "RIGHT", "BACKWARD", "UP"]))

def MoveToPos(pos):

    global CURRENT_POS

    CX, CY = CURRENT_POS

    NX, NY = pos

    if NX > CX:

        MX = NX - CX

        MXD = "D"

    elif NX < CX:

        MX = CX - NX

        MXD = "A"

    elif NX == CX:

        MX = 0

        MXD = "D"

    if NY > CY:

        MY = NY - CY

        MYD = "W"

    elif NY < CY:

        MY = CY - NY

        MYD = "S"

    elif NY == CY:

        MY = 0

        MYD = "W"

    print("Current position:", CX, CY)

    print("To move:", MX, MY)

    print("Directions:", MXD, MYD)

    Hotkey(MXD, round(MX / 20) if MX != 0 else 0)

    Hotkey(MYD, round(MY / 20) if MY != 0 else 0)

    CURRENT_POS = (NX, NY)

def resetPosition():

    global CURRENT_POS

    CURRENT_POS = (0, 0)
    