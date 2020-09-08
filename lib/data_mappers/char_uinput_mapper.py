# Author: Jan Subelj
# Contribution: Jez Mckinley (https://github.com/tabashir/g910-gkey-macro-support)

import uinput


def click(uinput_key):
    return [(uinput_key, 3)]


def wrap_shift(key_array):
    return [(uinput.KEY_LEFTSHIFT, 1)] + key_array + [(uinput.KEY_LEFTSHIFT, 0)]


def wrap_altgr(key_array):
    return [(uinput.KEY_RIGHTALT, 1)] + key_array + [(uinput.KEY_RIGHTALT, 0)]


# types of return events: list(touple(uinputkey, [0,1,3])) ex: [((1,12),0),((1,12),1), ((1,12),3)]
# 1 means keypress
# 0 means keyrelease
# 3 means click key
keys = {
    "control": {
        'ctrl': click(uinput.KEY_LEFTCTRL),
        'alt': click(uinput.KEY_LEFTALT),
        'altgr': click(uinput.KEY_RIGHTALT),
        'win': click(uinput.KEY_LEFTMETA),
        'home': click(uinput.KEY_HOME),
        'delete': click(uinput.KEY_DELETE),
        'pageup': click(uinput.KEY_PAGEUP),
        'pagedown': click(uinput.KEY_PAGEDOWN),
        "shift": click(uinput.KEY_LEFTSHIFT),
        'esc': click(uinput.KEY_ESC),
        "enter": click(uinput.KEY_ENTER),
        "capslock": click(uinput.KEY_CAPSLOCK),

        # keypad
        "NUM0": click(uinput.KEY_KP0),
        "NUM1": click(uinput.KEY_KP1),
        "NUM2": click(uinput.KEY_KP2),
        "NUM3": click(uinput.KEY_KP3),
        "NUM4": click(uinput.KEY_KP4),
        "NUM5": click(uinput.KEY_KP5),
        "NUM6": click(uinput.KEY_KP6),
        "NUM7": click(uinput.KEY_KP7),
        "NUM8": click(uinput.KEY_KP8),
        "NUM9": click(uinput.KEY_KP9),
        "NUM-": click(uinput.KEY_KPMINUS),
        "NUMPLUS": click(uinput.KEY_KPPLUS),
        "NUM/": click(uinput.KEY_KPSLASH),
        "NUM*": click(uinput.KEY_KPASTERISK),
        "NUMCOMMA": click(uinput.KEY_KPCOMMA),
        "NUM.": click(uinput.KEY_KPDOT),
        "NUMENTER": click(uinput.KEY_KPENTER),
        "NUMLOCK": click(uinput.KEY_NUMLOCK),

        'F1': click(uinput.KEY_F1),
        'F2': click(uinput.KEY_F2),
        'F3': click(uinput.KEY_F3),
        'F4': click(uinput.KEY_F4),
        'F5': click(uinput.KEY_F5),
        'F6': click(uinput.KEY_F6),
        'F7': click(uinput.KEY_F7),
        'F8': click(uinput.KEY_F8),
        'F9': click(uinput.KEY_F9),
        'F10': click(uinput.KEY_F10),
        'F11': click(uinput.KEY_F11),
        'F12': click(uinput.KEY_F12),
        'F13': click(uinput.KEY_F13),
        'F14': click(uinput.KEY_F14),
        'F15': click(uinput.KEY_F15),
        'F16': click(uinput.KEY_F16),
        'F17': click(uinput.KEY_F17),
        'F18': click(uinput.KEY_F18),
        'PLUSMINUS': click(uinput.KEY_KPPLUSMINUS),
        'STOP': click(uinput.KEY_STOP),
        'AGAIN': click(uinput.KEY_AGAIN),
        'PROPS': click(uinput.KEY_PROPS),
        'FRONT': click(uinput.KEY_FRONT),
        'UNDO': click(uinput.KEY_UNDO),
    },
    "si": {

        # autogenerated
        '0': click(uinput.KEY_0),
        '1': click(uinput.KEY_1),
        '2': click(uinput.KEY_2),
        '3': click(uinput.KEY_3),
        '4': click(uinput.KEY_4),
        '5': click(uinput.KEY_5),
        '6': click(uinput.KEY_6),
        '7': click(uinput.KEY_7),
        '8': click(uinput.KEY_8),
        '9': click(uinput.KEY_9),
        'a': click(uinput.KEY_A),
        'A': wrap_shift(click(uinput.KEY_A)),
        'b': click(uinput.KEY_B),
        'B': wrap_shift(click(uinput.KEY_B)),
        'c': click(uinput.KEY_C),
        'C': wrap_shift(click(uinput.KEY_C)),
        'd': click(uinput.KEY_D),
        'D': wrap_shift(click(uinput.KEY_D)),
        'e': click(uinput.KEY_E),
        'E': wrap_shift(click(uinput.KEY_E)),
        'f': click(uinput.KEY_F),
        'F': wrap_shift(click(uinput.KEY_F)),
        'g': click(uinput.KEY_G),
        'G': wrap_shift(click(uinput.KEY_G)),
        'h': click(uinput.KEY_H),
        'H': wrap_shift(click(uinput.KEY_H)),
        'i': click(uinput.KEY_I),
        'I': wrap_shift(click(uinput.KEY_I)),
        'j': click(uinput.KEY_J),
        'J': wrap_shift(click(uinput.KEY_J)),
        'k': click(uinput.KEY_K),
        'K': wrap_shift(click(uinput.KEY_K)),
        'l': click(uinput.KEY_L),
        'L': wrap_shift(click(uinput.KEY_L)),
        'm': click(uinput.KEY_M),
        'M': wrap_shift(click(uinput.KEY_M)),
        'n': click(uinput.KEY_N),
        'N': wrap_shift(click(uinput.KEY_N)),
        'o': click(uinput.KEY_O),
        'O': wrap_shift(click(uinput.KEY_O)),
        'p': click(uinput.KEY_P),
        'P': wrap_shift(click(uinput.KEY_P)),
        'q': click(uinput.KEY_Q),
        'Q': wrap_shift(click(uinput.KEY_Q)),
        'r': click(uinput.KEY_R),
        'R': wrap_shift(click(uinput.KEY_R)),
        's': click(uinput.KEY_S),
        'S': wrap_shift(click(uinput.KEY_S)),
        't': click(uinput.KEY_T),
        'T': wrap_shift(click(uinput.KEY_T)),
        'u': click(uinput.KEY_U),
        'U': wrap_shift(click(uinput.KEY_U)),
        'v': click(uinput.KEY_V),
        'V': wrap_shift(click(uinput.KEY_V)),
        'w': click(uinput.KEY_W),
        'W': wrap_shift(click(uinput.KEY_W)),
        'x': click(uinput.KEY_X),
        'X': wrap_shift(click(uinput.KEY_X)),

        # none universal keyboard
        'z': click(uinput.KEY_Y),
        'Z': wrap_shift(click(uinput.KEY_Y)),
        'y': click(uinput.KEY_Z),
        'Y': wrap_shift(click(uinput.KEY_Z)),

        # gen from 0 to 9 by get_shift_keys():
        '=': wrap_shift(click(uinput.KEY_0)),
        '!': wrap_shift(click(uinput.KEY_1)),
        '"': wrap_shift(click(uinput.KEY_2)),
        '#': wrap_shift(click(uinput.KEY_3)),
        '$': wrap_shift(click(uinput.KEY_4)),
        '%': wrap_shift(click(uinput.KEY_5)),
        '&': wrap_shift(click(uinput.KEY_6)),
        '/': wrap_shift(click(uinput.KEY_7)),
        '(': wrap_shift(click(uinput.KEY_8)),
        ')': wrap_shift(click(uinput.KEY_9)),

        # gen with get_altgr_keys():
        '˝': wrap_altgr(click(uinput.KEY_0)) + click(uinput.KEY_SPACE),
        '~': wrap_altgr(click(uinput.KEY_1)) + click(uinput.KEY_SPACE),
        'ˇ': wrap_altgr(click(uinput.KEY_2)) + click(uinput.KEY_SPACE),
        '^': wrap_altgr(click(uinput.KEY_3)) + click(uinput.KEY_SPACE),
        '˘': wrap_altgr(click(uinput.KEY_4)) + click(uinput.KEY_SPACE),
        '°': wrap_altgr(click(uinput.KEY_5)) + click(uinput.KEY_SPACE),
        '˛': wrap_altgr(click(uinput.KEY_6)) + click(uinput.KEY_SPACE),
        '`': wrap_altgr(click(uinput.KEY_7)) + click(uinput.KEY_SPACE),
        '˙': wrap_altgr(click(uinput.KEY_8)) + click(uinput.KEY_SPACE),

        # gen with get other keys:
        "'": click(uinput.KEY_MINUS),
        '¸': click(uinput.KEY_GRAVE),
        'č': click(uinput.KEY_SEMICOLON),
        'ć': click(uinput.KEY_APOSTROPHE),
        'š': click(uinput.KEY_LEFTBRACE),
        'ž': click(uinput.KEY_BACKSLASH),
        'đ': click(uinput.KEY_RIGHTBRACE),

        ',': click(uinput.KEY_COMMA),
        '.': click(uinput.KEY_DOT),
        '-': click(uinput.KEY_SLASH),
        '*': click(uinput.KEY_KPASTERISK),
        ' ': click(uinput.KEY_SPACE),

        # gen with get other keys with shift:
        '?': wrap_shift(click(uinput.KEY_MINUS)),
        'Š': wrap_shift(click(uinput.KEY_LEFTBRACE)),
        'Đ': wrap_shift(click(uinput.KEY_RIGHTBRACE)),
        'Č': wrap_shift(click(uinput.KEY_SEMICOLON)),
        'Ć': wrap_shift(click(uinput.KEY_APOSTROPHE)),
        '¨': wrap_shift(click(uinput.KEY_GRAVE)),
        'Ž': wrap_shift(click(uinput.KEY_BACKSLASH)),
        ';': wrap_shift(click(uinput.KEY_COMMA)),
        ':': wrap_shift(click(uinput.KEY_DOT)),
        '_': wrap_shift(click(uinput.KEY_SLASH)),

        # gen with get other keys with altgr:
        '\\': wrap_altgr(click(uinput.KEY_Q)),
        '|': wrap_altgr(click(uinput.KEY_W)),
        '€': wrap_altgr(click(uinput.KEY_E)),
        '¶': wrap_altgr(click(uinput.KEY_R)),
        'ŧ': wrap_altgr(click(uinput.KEY_T)),
        '←': wrap_altgr(click(uinput.KEY_Y)),
        '↓': wrap_altgr(click(uinput.KEY_U)),
        '→': wrap_altgr(click(uinput.KEY_I)),
        'ø': wrap_altgr(click(uinput.KEY_O)),
        'þ': wrap_altgr(click(uinput.KEY_P)),
        '÷': wrap_altgr(click(uinput.KEY_LEFTBRACE)),
        '×': wrap_altgr(click(uinput.KEY_RIGHTBRACE)),
        'æ': wrap_altgr(click(uinput.KEY_A)),
        '„': wrap_altgr(click(uinput.KEY_S)),
        '“': wrap_altgr(click(uinput.KEY_D)),
        '[': wrap_altgr(click(uinput.KEY_F)),
        ']': wrap_altgr(click(uinput.KEY_G)),
        'ħ': wrap_altgr(click(uinput.KEY_H)),
        'ł': wrap_altgr(click(uinput.KEY_L)),
        'ß': wrap_altgr(click(uinput.KEY_APOSTROPHE)),
        '¤': wrap_altgr(click(uinput.KEY_BACKSLASH)),
        '‘': wrap_altgr(click(uinput.KEY_Z)),
        '’': wrap_altgr(click(uinput.KEY_X)),
        '¢': wrap_altgr(click(uinput.KEY_C)),
        '@': wrap_altgr(click(uinput.KEY_V)),
        '{': wrap_altgr(click(uinput.KEY_B)),
        '}': wrap_altgr(click(uinput.KEY_N)),
        '<': click(uinput.KEY_102ND),
        '>': wrap_shift(click(uinput.KEY_102ND)),
        '—': wrap_altgr(click(uinput.KEY_SLASH)),
        '→': click(uinput.KEY_RIGHT),
        '←': click(uinput.KEY_LEFT),
        '↑': click(uinput.KEY_UP),
        '↓': click(uinput.KEY_DOWN),
        '\t': click(uinput.KEY_TAB),
        '\n': click(uinput.KEY_ENTER),

    },
    'en': {
        '0': click(uinput.KEY_0),
        '1': click(uinput.KEY_1),
        '2': click(uinput.KEY_2),
        '3': click(uinput.KEY_3),
        '4': click(uinput.KEY_4),
        '5': click(uinput.KEY_5),
        '6': click(uinput.KEY_6),
        '7': click(uinput.KEY_7),
        '8': click(uinput.KEY_8),
        '9': click(uinput.KEY_9),
        'a': click(uinput.KEY_A),
        'A': wrap_shift(click(uinput.KEY_A)),
        'b': click(uinput.KEY_B),
        'B': wrap_shift(click(uinput.KEY_B)),
        'c': click(uinput.KEY_C),
        'C': wrap_shift(click(uinput.KEY_C)),
        'd': click(uinput.KEY_D),
        'D': wrap_shift(click(uinput.KEY_D)),
        'e': click(uinput.KEY_E),
        'E': wrap_shift(click(uinput.KEY_E)),
        'f': click(uinput.KEY_F),
        'F': wrap_shift(click(uinput.KEY_F)),
        'g': click(uinput.KEY_G),
        'G': wrap_shift(click(uinput.KEY_G)),
        'h': click(uinput.KEY_H),
        'H': wrap_shift(click(uinput.KEY_H)),
        'i': click(uinput.KEY_I),
        'I': wrap_shift(click(uinput.KEY_I)),
        'j': click(uinput.KEY_J),
        'J': wrap_shift(click(uinput.KEY_J)),
        'k': click(uinput.KEY_K),
        'K': wrap_shift(click(uinput.KEY_K)),
        'l': click(uinput.KEY_L),
        'L': wrap_shift(click(uinput.KEY_L)),
        'm': click(uinput.KEY_M),
        'M': wrap_shift(click(uinput.KEY_M)),
        'n': click(uinput.KEY_N),
        'N': wrap_shift(click(uinput.KEY_N)),
        'o': click(uinput.KEY_O),
        'O': wrap_shift(click(uinput.KEY_O)),
        'p': click(uinput.KEY_P),
        'P': wrap_shift(click(uinput.KEY_P)),
        'q': click(uinput.KEY_Q),
        'Q': wrap_shift(click(uinput.KEY_Q)),
        'r': click(uinput.KEY_R),
        'R': wrap_shift(click(uinput.KEY_R)),
        's': click(uinput.KEY_S),
        'S': wrap_shift(click(uinput.KEY_S)),
        't': click(uinput.KEY_T),
        'T': wrap_shift(click(uinput.KEY_T)),
        'u': click(uinput.KEY_U),
        'U': wrap_shift(click(uinput.KEY_U)),
        'v': click(uinput.KEY_V),
        'V': wrap_shift(click(uinput.KEY_V)),
        'w': click(uinput.KEY_W),
        'W': wrap_shift(click(uinput.KEY_W)),
        'x': click(uinput.KEY_X),
        'X': wrap_shift(click(uinput.KEY_X)),
        'y': click(uinput.KEY_Y),
        'Y': wrap_shift(click(uinput.KEY_Y)),
        'z': click(uinput.KEY_Z),
        'Z': wrap_shift(click(uinput.KEY_Z)),

        ')': wrap_shift(click(uinput.KEY_0)),
        '!': wrap_shift(click(uinput.KEY_1)),
        '@': wrap_shift(click(uinput.KEY_2)),
        '#': wrap_shift(click(uinput.KEY_3)),
        '$': wrap_shift(click(uinput.KEY_4)),
        '%': wrap_shift(click(uinput.KEY_5)),
        '^': wrap_shift(click(uinput.KEY_6)),
        '&': wrap_shift(click(uinput.KEY_7)),
        '(': wrap_shift(click(uinput.KEY_9)),

        '-': click(uinput.KEY_MINUS),
        '_': wrap_shift(click(uinput.KEY_MINUS)),
        '=': click(uinput.KEY_EQUAL),

        '\t': click(uinput.KEY_TAB),
        '[': click(uinput.KEY_LEFTBRACE),
        ']': click(uinput.KEY_RIGHTBRACE),
        '\n': click(uinput.KEY_ENTER),

        "'": click(uinput.KEY_APOSTROPHE),
        ";": click(uinput.KEY_SEMICOLON),
        ":": wrap_shift(click(uinput.KEY_SEMICOLON)),
        '"': wrap_shift(click(uinput.KEY_APOSTROPHE)),
        '`': click(uinput.KEY_GRAVE),
        '\\': click(uinput.KEY_BACKSLASH),
        ',': click(uinput.KEY_COMMA),
        '.': click(uinput.KEY_DOT),
        '/': click(uinput.KEY_SLASH),

        '*': click(uinput.KEY_KPASTERISK),

        ' ': click(uinput.KEY_SPACE),
        '±': click(uinput.KEY_KPPLUSMINUS),
    },
    'de': {
        '0': click(uinput.KEY_0),
        '1': click(uinput.KEY_1),
        '2': click(uinput.KEY_2),
        '3': click(uinput.KEY_3),
        '4': click(uinput.KEY_4),
        '5': click(uinput.KEY_5),
        '6': click(uinput.KEY_6),
        '7': click(uinput.KEY_7),
        '8': click(uinput.KEY_8),
        '9': click(uinput.KEY_9),
        'a': click(uinput.KEY_A),
        'A': wrap_shift(click(uinput.KEY_A)),
        'b': click(uinput.KEY_B),
        'B': wrap_shift(click(uinput.KEY_B)),
        'c': click(uinput.KEY_C),
        'C': wrap_shift(click(uinput.KEY_C)),
        'd': click(uinput.KEY_D),
        'D': wrap_shift(click(uinput.KEY_D)),
        'e': click(uinput.KEY_E),
        'E': wrap_shift(click(uinput.KEY_E)),
        'f': click(uinput.KEY_F),
        'F': wrap_shift(click(uinput.KEY_F)),
        'g': click(uinput.KEY_G),
        'G': wrap_shift(click(uinput.KEY_G)),
        'h': click(uinput.KEY_H),
        'H': wrap_shift(click(uinput.KEY_H)),
        'i': click(uinput.KEY_I),
        'I': wrap_shift(click(uinput.KEY_I)),
        'j': click(uinput.KEY_J),
        'J': wrap_shift(click(uinput.KEY_J)),
        'k': click(uinput.KEY_K),
        'K': wrap_shift(click(uinput.KEY_K)),
        'l': click(uinput.KEY_L),
        'L': wrap_shift(click(uinput.KEY_L)),
        'm': click(uinput.KEY_M),
        'M': wrap_shift(click(uinput.KEY_M)),
        'n': click(uinput.KEY_N),
        'N': wrap_shift(click(uinput.KEY_N)),
        'o': click(uinput.KEY_O),
        'O': wrap_shift(click(uinput.KEY_O)),
        'p': click(uinput.KEY_P),
        'P': wrap_shift(click(uinput.KEY_P)),
        'q': click(uinput.KEY_Q),
        'Q': wrap_shift(click(uinput.KEY_Q)),
        'r': click(uinput.KEY_R),
        'R': wrap_shift(click(uinput.KEY_R)),
        's': click(uinput.KEY_S),
        'S': wrap_shift(click(uinput.KEY_S)),
        't': click(uinput.KEY_T),
        'T': wrap_shift(click(uinput.KEY_T)),
        'u': click(uinput.KEY_U),
        'U': wrap_shift(click(uinput.KEY_U)),
        'v': click(uinput.KEY_V),
        'V': wrap_shift(click(uinput.KEY_V)),
        'w': click(uinput.KEY_W),
        'W': wrap_shift(click(uinput.KEY_W)),
        'x': click(uinput.KEY_X),
        'X': wrap_shift(click(uinput.KEY_X)),
        'y': click(uinput.KEY_Z),
        'Y': wrap_shift(click(uinput.KEY_Z)),
        'z': click(uinput.KEY_Y),
        'Z': wrap_shift(click(uinput.KEY_Y)),

        '=': wrap_shift(click(uinput.KEY_0)),
        '!': wrap_shift(click(uinput.KEY_1)),
        '"': wrap_shift(click(uinput.KEY_2)),
        '§': wrap_shift(click(uinput.KEY_3)),
        '$': wrap_shift(click(uinput.KEY_4)),
        '%': wrap_shift(click(uinput.KEY_5)),
        '&': wrap_shift(click(uinput.KEY_6)),
        '/': wrap_shift(click(uinput.KEY_7)),
        '(': wrap_shift(click(uinput.KEY_8)),
        ')': wrap_shift(click(uinput.KEY_9)),

        '}': wrap_altgr(click(uinput.KEY_0)),
        '{': wrap_altgr(click(uinput.KEY_7)),
        '[': wrap_altgr(click(uinput.KEY_8)),
        ']': wrap_altgr(click(uinput.KEY_9)),

        '<': click(uinput.KEY_102ND),
        '>': wrap_shift(click(uinput.KEY_102ND)),
        '|': wrap_altgr(click(uinput.KEY_102ND)),

        'ß': click(uinput.KEY_MINUS),
        '?': wrap_shift(click(uinput.KEY_MINUS)),
        '\\': wrap_altgr(click(uinput.KEY_MINUS)),

        '+': click(uinput.KEY_RIGHTBRACE),
        '*': wrap_shift(click(uinput.KEY_RIGHTBRACE)),
        '~': wrap_altgr(click(uinput.KEY_RIGHTBRACE)),

        '#': click(uinput.KEY_BACKSLASH),

        ',': click(uinput.KEY_COMMA),
        ';': wrap_shift(click(uinput.KEY_COMMA)),

        '.': click(uinput.KEY_DOT),
        ':': wrap_shift(click(uinput.KEY_DOT)),

        '-': click(uinput.KEY_SLASH),
        '_': wrap_shift(click(uinput.KEY_SLASH)),

        'ö': click(uinput.KEY_SEMICOLON),
        'Ö': wrap_shift(click(uinput.KEY_SEMICOLON)),
        'ä': click(uinput.KEY_APOSTROPHE),
        'Ä': wrap_shift(click(uinput.KEY_APOSTROPHE)),
        'ü': click(uinput.KEY_LEFTBRACE),
        'Ü': wrap_shift(click(uinput.KEY_LEFTBRACE)),

        '\t': click(uinput.KEY_TAB),
        '\n': click(uinput.KEY_ENTER),
        
    }
}

key_names = [i for i in dir(uinput) if i.isupper() and not i.startswith("_")]
reverse_keys = {getattr(uinput, j): j for j in key_names}

if __name__ == "__main__":
    print(reverse_keys)
    print(keys["si"].keys())
    print(keys["en"].keys())
    print(keys["control"].keys())
