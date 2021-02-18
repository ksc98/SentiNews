import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

    B_BLACK = '\u001b[30;1m'
    B_RED = '\u001b[31;1m'
    B_GREEN = '\u001b[32;1m'
    B_YELLOW = '\u001b[33;1m'
    B_BLUE = '\u001b[34;1m'
    B_MAGENTA = '\u001b[35;1m'
    B_CYAN = '\u001b[36;1m'
    B_WHITE = '\u001b[37;1m'


def blue(s): return style.BLUE + s + style.RESET
def black(s): return style.BLACK + s + style.RESET
def red(s): return style.RED + s + style.RESET
def green(s): return style.GREEN + s + style.RESET
def yellow(s): return style.YELLOW + s + style.RESET
def underline(s): return style.UNDERLINE + s + style.RESET
def magenta(s): return style.MAGENTA + s + style.RESET
def cyan(s): return style.CYAN + s + style.RESET
def white(s): return style.WHITE + s + style.RESET

def b_blue(s): return style.B_BLUE + s + style.RESET
def b_black(s): return style.B_BLACK + s + style.RESET
def b_red(s): return style.B_RED + s + style.RESET
def b_green(s): return style.B_GREEN + s + style.RESET
def b_yellow(s): return style.B_YELLOW + s + style.RESET
def b_magenta(s): return style.B_MAGENTA + s + style.RESET
def b_cyan(s): return style.B_CYAN + s + style.RESET
def b_white(s): return style.B_WHITE + s + style.RESET
