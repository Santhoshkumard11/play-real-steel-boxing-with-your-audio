from typing import Callable
from helpers.utils import *


def make_move(text):
    """Make the move

    Args:
        text (str): text from the deepgram api
    """

    print(f"Received -  {text}")

    text: str = clean_text(text)

    callable_action_method: Callable = globals()[text]
    print(f"Executing - {callable_action_method.__name__}")

    callable_action_method()
