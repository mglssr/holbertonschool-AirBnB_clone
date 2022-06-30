#!/usr/bin/python3
"""program called console.py that contains the entry 
point of the command interpreter"""


import cmd, sys
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
        """Creates a new instance of BaseModel, 
        saves it (to the JSON file) and prints the id"""
        if len(arg) < 1:
            print(f"** class name missing **")
        a_list = arg.split()
        if a_list[0] in self.classes:
            to_get = getattr(sys.modules[__name__], arg)
            n_inst = to_get()
            print(n_inst.id)
            n_inst.save()
        else:
            print(f"** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        a_list = arg.split()
        if len(a_list) < 1:
            print(f"** class name missing **")
        if len(a_list) == 1:
            if a_list in self.classes:
                print(f"** instance id missing **")
            else:
                print(f"** class name missing **")
        if a_list[0] in self.classes:
            key = f"{a_list[0]}.{a_list[1]}"
            aux_dict = storage.all()
            if key in aux_dict:
                print(aux_dict[key])
            else:
                print(f"** no instance found **")
        else:
            print(f"** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)"""
        a_list =arg.split()
        if len(a_list) < 1:
            print(f"")
        elif len(a_list) == 1:
            if a_list in self.classes:
                print(f"** instance id missing **")
            else:
                print(f"** class name missing **")
        else:
            if a_list[0] in self.classes:
                aux_dict = storage.all()
                key = f"{a_list[0]}.{a_list[1]}"
                if key in aux_dict:
                    del aux_dict[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        a_list = arg.split()
        if len(a_list) < 1:
            aux_dict = storage.all()
            v_list=[]
            for key in aux_dict:
                elem = aux_dict[key]
                v_list.append(elem)
            print(v_list)

if __name__ == '__main__': 
    HBNBCommand().cmdloop()
