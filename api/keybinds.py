# Modules
import time
import ctypes

from sys import argv
from ctypes import wintypes

from .windows import WindowManager

# Initialization
HANDLER = WindowManager()

user32 = ctypes.WinDLL("user32", use_last_error = True)

SHIFT          = 0x10

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

ALPHABET = {
    "0": 0x30,
    "1": 0x31,
    "2": 0x32,
    "3": 0x33,
    "4": 0x34,
    "5": 0x35,
    "6": 0x36,
    "7": 0x37,
    "8": 0x38,
    "9": 0x39,
    "A": 0x41,
    "B": 0x42,
    "C": 0x43,
    "D": 0x44,
    "E": 0x45,
    "F": 0x46,
    "G": 0x47,
    "H": 0x48,
    "I": 0x49,
    "J": 0x4A,
    "K": 0x4B,
    "L": 0x4C,
    "M": 0x4D,
    "N": 0x4E,
    "O": 0x4F,
    "P": 0x50,
    "Q": 0x51,
    "R": 0x52,
    "S": 0x53,
    "T": 0x54,
    "U": 0x55,
    "V": 0x56,
    "W": 0x57,
    "X": 0x58,
    "Y": 0x59,
    "Z": 0x5A,
    " ": 0x20,
    "/": 0xBF,
    ",": 0xBC,
    ".": 0xBE,
    ";": 0xBA,
    "[ENTER]": 0x0D,
    "[ESC]": 0x1B
}

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12

# C Structures
wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):

    _fields_ = (
        ("dx",          wintypes.LONG),
        ("dy",          wintypes.LONG),
        ("mouseData",   wintypes.DWORD),
        ("dwFlags",     wintypes.DWORD),
        ("time",        wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR)
    )

class KEYBDINPUT(ctypes.Structure):

    _fields_ = (
        ("wVk",         wintypes.WORD),
        ("wScan",       wintypes.WORD),
        ("dwFlags",     wintypes.DWORD),
        ("time",        wintypes.DWORD),
        ("dwExtraInfo", wintypes.ULONG_PTR)
    )

    def __init__(self, *args, **kwds):

        super(KEYBDINPUT, self).__init__(*args, **kwds)

        if not self.dwFlags & KEYEVENTF_UNICODE:

            self.wScan = user32.MapVirtualKeyExW(
                self.wVk,
                MAPVK_VK_TO_VSC,
                0
            )

class HARDWAREINPUT(ctypes.Structure):

    _fields_ = (
        ("uMsg",    wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD)
    )

class INPUT(ctypes.Structure):

    class _INPUT(ctypes.Union):

        _fields_ = (
            ("ki", KEYBDINPUT),
            ("mi", MOUSEINPUT),
            ("hi", HARDWAREINPUT)
        )

    _anonymous_ = ("_input",)

    _fields_ = (
        ("type",   wintypes.DWORD),
        ("_input", _INPUT)
    )

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):

    if result == 0:

        raise ctypes.WinError(ctypes.get_last_error())

    return args

user32.SendInput.errcheck = _check_count

user32.SendInput.argtypes = (
    wintypes.UINT,
    LPINPUT,
    ctypes.c_int
)

# Functions
def PressKey(hexKeyCode):

    # Focus on ROBLOX only
    HANDLER.focusROBLOX()

    x = INPUT(
        type = INPUT_KEYBOARD,
        ki = KEYBDINPUT(wVk = hexKeyCode)
    )

    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    
    x = INPUT(
        type = INPUT_KEYBOARD,
        ki = KEYBDINPUT(
            wVk = hexKeyCode,
            dwFlags = KEYEVENTF_KEYUP
        )
    )

    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def AltTab():

    PressKey(VK_MENU)

    PressKey(VK_TAB)

    ReleaseKey(VK_TAB)
    
    time.sleep(2)

    ReleaseKey(VK_MENU)

def Type(text):

    textCodes = []

    isCaps = []

    for char in text:

        textCodes.append(ALPHABET[char.upper()])

        if char.upper() == char and not char in ["/", ".", ","]:

            isCaps.append(True)

        else:

            isCaps.append(False)

    c = 0

    for textCode in textCodes:

        if isCaps[c]:

            PressKey(SHIFT)

        PressKey(textCode)

        ReleaseKey(textCode)

        if isCaps[c]:

            ReleaseKey(SHIFT)

        c += 1

def Hotkey(key, seconds = 0):

    HANDLER.focusROBLOX()

    code = ALPHABET[key]

    time.sleep(.1)

    PressKey(code)

    time.sleep(seconds)

    ReleaseKey(code)

def Chat(text):

    if "-q" in argv[1:] or "--quiet" in argv[1:]:

        return

    Type("/")

    time.sleep(.5)

    Type(text)

    Hotkey("[ENTER]", .35)
