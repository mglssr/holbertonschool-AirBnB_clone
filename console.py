#!/usr/bin/python3
"""program called console.py that contains the entry 
point of the command interpreter"""


import cmd


class HBNBCommand(cmd.Cmd):
    """a"""
    prompt = '(hbnb)'


    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
