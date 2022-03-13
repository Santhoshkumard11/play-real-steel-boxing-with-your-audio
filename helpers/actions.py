from typing import Callable
from helpers.utils import *
import logging


def make_move(text):
    """Get a single command name from the transcribed text and call the corresponding command

    Args:
        text (str): text from the deepgram api
    """

    logging.info(f"Received -  {text}")

    text: str = clean_text(text)

    callable_action_method: Callable = globals()[text]
    logging.info(f"Executing - {callable_action_method.__name__}")

    callable_action_method()
