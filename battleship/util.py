import os
from sys import platform

IS_NOT_HIT = 0
IS_HIT = 1
IS_SUNK = 2


def clear_screen():
    os.system("cls") if platform == "win32" else os.system("clear")
