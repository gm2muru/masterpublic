import os
import re


def myHiDef(name):
    """Welcome a person by printing his/her name

    Args:
        name (string): Name
    """
    print(f "myHi {name}")
    insideMyHi()


def insideMyHi():
    print("myHi")
    print("myHi")
    print("myHi")
    print("myHi")
    print("myHi")


myHiDef("Muru")
print("Hi")
print("Hi")
print("Hi")
print("Hi")
