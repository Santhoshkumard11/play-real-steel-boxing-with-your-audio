from pyautogui import moveTo, click, press, hotkey
from time import sleep
from helpers._constants import COMMANDS_AUDIO_MAPPING


def left_jab():
    press("j")


def left_hook():
    hotkey("a", "j")


def right_jab():
    hotkey("s", "j")


def right_powerful():
    hotkey("s", "j")


def block():
    press("l")


def special_move():
    press("o")


def dash_back():
    press("a", 2, 0.1)


def dash_forward():
    press("d", 2, 0.1)


def advance():
    press("d")


def dodge():
    press("w", 2, 0.1)


def dodge_left():
    press("d", 2, 0.1)


def step_back():
    press("a", 2, 0.1)


def double_upper_cut():
    hotkey("s", "i")


def engage():
    advance()
    left_hook()
    right_jab()
    left_jab()
    right_powerful()


def clean_text(text: str):

    for action, method_name in COMMANDS_AUDIO_MAPPING.items():

        if text.find(action) != -1:

            return method_name

    # if nothing matchs we just move the bot back (a defensive move)
    return "step_back"
