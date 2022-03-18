KEYWORDS = [
    "back step",
    "upper cut",
    "advance",
    "engage",
    "left",
    "right",
    "dodge",
    "block",
    "dash",
    "dash back",
    "arms up",
    "left hook",
    "right hook",
    "special move",
    "left jab",
    "right jab",
    "right upper cut",
    "jab",
    "dash forward",
]

"""
Game Controles:
Dash Forward - d + d
Dash Backword - a + a
Dodge Right - s + s
Dodge Left - w + w
Jab - j
Cross (straight) - d + j
Right Hook - w + j
Left lower hook - a + j
Right lower cut - s + j
Left Upper cut - i
right aggressive - d + i
Right Powerful - a + i
Double upper cut - s + i
Turbo Powerful = w + i
Block - l
Special Move - o
Center tap - u
"""

COMMANDS_AUDIO_MAPPING = {
    "dodge": "dodge",
    "dodge right": "dodge",
    "dodge left": "dodge_left",
    "left hook": "left_hook",
    "advance": "advance",
    "dash back": "dash_back",
    "dash forward": "dash_forward",
    "dash": "dash_forward",
    "arms up": "block",
    "special block": "special_move_block",
    "special move": "special_move",
    "special": "special_move",
    "thumbs up": "block",
    "left hook": "left_hook",
    "engage": "engage",
    "double upper cut": "double_upper_cut",
    "right hook": "right_powerful",
    "step back": "step_back",
    "lean back": "step_back",
    "times twenty": "times_20",
    "block": "block",
    "rock": "block",
    "lock": "block",
    "cover up": "block",
    "combo": "aggressive",
    "left": "left_jab",
    "left jab": "left_jab",
    "counter left": "left_jab",
    "left jam": "left_jab",
    "left jump": "left_jab",
    "left job": "left_jab",
    "right jab": "right_jab",
    "right job": "right_jab",
    "right jam": "right_jab",
    "right": "right_jab",
}
