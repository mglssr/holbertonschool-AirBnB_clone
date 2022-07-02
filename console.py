#!/usr/bin/python3
"""Program called console.py that contains the entry
point of the command interpreter"""


import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class that"""
    prompt = '(hbnb) '
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "Amenity": Amenity, "City": City, "Place": Place,
               "Review": Review}

    def emptyline(self):
        """Dont' execute anything if an empty line + ENTER are typed"""
        pass

    def do_quit(self, arg):
        """quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF (Ctrl+D) to exit the program"""
        return True

    """def precmd(self, arg):
        a_list = arg.split('.')
        if len(a_list) == 2:
            if a_list[1] == "all()":
                if a_list[0] in self.classes:
                    self.do_all(a_list[0])
            if a_list[1] == "count()":
                if a_list[0] in self.classes:
                    self.do_count(a_list[0])"""

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        a_list = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif a_list[0] in self.classes:
            to_get = getattr(sys.modules[__name__], a_list[0])
            n_inst = to_get()
            print(n_inst.id)
            n_inst.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        a_list = arg.split()
        if len(a_list) < 1:
            print("** class name missing **")
        elif len(a_list) == 1:
            if a_list[0] in self.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if a_list[0] in self.classes:
                key = f"{a_list[0]}.{a_list[1]}"
                aux_dict = storage.all()
                if key in aux_dict:
                    print(aux_dict[key])
                else:
                    print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file)"""
        a_list = arg.split()
        if len(a_list) < 1:
            print("** class name missing **")
        elif len(a_list) == 1:
            if a_list[0] in self.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            if a_list[0] in self.classes:
                aux_dict = storage.all()
                key = f"{a_list[0]}.{a_list[1]}"
                if key in aux_dict:
                    del aux_dict[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        a_list = arg.split()
        aux_dict = storage.all()
        v_list = []
        if len(a_list) < 1:
            for key in aux_dict:
                elem = aux_dict[key]
                v_list.append(str(elem))
            print(v_list)
        else:
            if a_list[0] in self.classes:
                for key, value in aux_dict.items():
                    if a_list[0] == value.__class__.__name__:
                        elem = aux_dict[key]
                        v_list.append(str(elem))
                print(v_list)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and
        id by adding or updating attribute (save the change
        into the JSON file)"""
        aux_dict = storage.all()
        a_list = arg.split()
        if len(a_list) < 1:
            print("** class name missing **")
        elif len(a_list) == 1:
            if a_list[0] in self.classes:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(a_list) == 2:
            if a_list[0] in self.classes:
                key = f"{a_list[0]}.{a_list[1]}"
                if key not in aux_dict:
                    print("** no instance found **")
                else:
                    print("** attribute name missing **")
            else:
                print("** class doesn't exist **")
        elif len(a_list) == 3:
            if a_list[0] in self.classes:
                key = f"{a_list[0]}.{a_list[1]}"
                if key not in aux_dict:
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** class doesn't exist **")
        else:
            key = f"{a_list[0]}.{a_list[1]}"
            if key in aux_dict:
                obj = aux_dict[key]
                setattr(obj, a_list[2], eval(a_list[3]))

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        counter = 0
        aux_dict = storage.all()
        a_list = arg.split()
        for key in aux_dict:
            if (a_list[0] in key):
                counter += 1
        print(counter)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
