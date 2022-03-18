from pyautogui import press, hotkey, keyDown, keyUp
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
    keyDown("l")
    sleep(2)
    keyUp("l")


def special_move():
    press("o")


def dash_back():
    press("a", 2, 0.1)


def dash_forward():
    press("d", 2, 0.1)


def advance():
    keyDown("d")
    sleep(1)
    keyUp("d")


def dodge():
    press("w", 2, 0.1)


def dodge_left():
    press("d", 2, 0.1)


def step_back():
    press("a", 2, 0.1)


def double_upper_cut():
    hotkey("s", "i")


def special_move_block():
    press("u", 10, 0.5)


def engage():
    left_hook()
    sleep(0.3)
    right_jab()
    sleep(0.3)
    left_jab()
    sleep(0.3)
    right_powerful()


def aggressive():
    advance()
    left_hook()
    sleep(0.3)
    right_jab()
    dodge()
    sleep(0.3)
    left_jab()
    sleep(0.3)
    right_powerful()
    advance()
    left_hook()
    dodge()
    sleep(0.3)
    right_jab()
    sleep(0.3)
    left_jab()
    sleep(0.3)
    right_powerful()


def times_20():
    for _ in range(20):
        press("j")
        sleep(0.1)
        press("i")
        hotkey("s", "j")


def clean_text(text: str):
    """Scan through the list of phrases and pick the best match

    Args:
        text (str): text from deepgram

    Returns:
        str: method name to the corresponding command
    """

    for action, method_name in COMMANDS_AUDIO_MAPPING.items():

        if text.find(action) != -1:

            return method_name

    # if nothing matchs we just move the bot back (a defensive move)
    return "step_back"
