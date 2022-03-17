from typing import Callable
from helpers.utils import (
    left_jab,
    left_hook,
    right_jab,
    right_powerful,
    block,
    special_move,
    dash_back,
    dash_forward,
    advance,
    dodge,
    dodge_left,
    step_back,
    double_upper_cut,
    special_move_block,
    engage,
    aggressive,
    times_20,
    clean_text
)

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
