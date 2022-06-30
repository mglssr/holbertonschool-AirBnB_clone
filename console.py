#!/usr/bin/python3
"""program called console.py that contains the entry 
point of the command interpreter"""


import cmd, sys, json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """a"""
    prompt = '(hbnb)'

    classes = {"BaseModel": BaseModel, "User": User, "State": State,
    "Amenity": Amenity, "City": City, "Place": Place, "Review": Review}

    def do_quit(self, arg):
        return True

    def do_EOF(self, arg):
        return True

    def do_create(self, arg):
        a_list = arg.split()
        if len(a_list) == 0:
            print(f"** class name missing **")
        if a_list[0] in self.classes:
            to_get = getattr(sys.modules[__name__], arg)
            n_instance = to_get()
            print(n_instance.id)
            n_instance.save()
        else:
            print(f"** class doesn't exist **")

    def do_show(self, arg):
        a_list = arg.split()
        if len(a_list) == 0:
            print(f"** class name missing **")
        if len(a_list) == 1:
            print(f"** instance id missing **")
        if a_list[0] in self.classes:
            key = f"{a_list[0]}.{a_list[1]}"
            inst = storage.all()
            if key in inst:
                print(inst[key])
        else:
            print(f"** class doesn't exist **")

        
if __name__ == '__main__': 
    HBNBCommand().cmdloop()
