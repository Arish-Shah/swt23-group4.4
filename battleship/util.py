import os
from sys import platform

IS_NOT_HIT = 0
IS_HIT = 1
IS_SUNK = 2

def clear_screen():
    if platform == "linux":
       os.system("clear") 
    os.system("cls")
