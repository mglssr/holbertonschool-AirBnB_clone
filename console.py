#!/usr/bin/python3
"""program called console.py that contains the entry 
point of the command interpreter"""


import cmd, sys
from models.user import User


class HBNBCommand(cmd.Cmd):
    """a"""
    prompt = '(hbnb)'

    def do_quit(self, line):
        return True

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
