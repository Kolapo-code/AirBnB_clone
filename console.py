#!/usr/bin/env python3
"""
Entry point of the command interpreter.
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "
    l_classes = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_quit(self, arg):
        """Quit command to exit the program"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in HBNBCommand.l_classes and cnd[0] in HBNBCommand.l_c:
                arg = cnd[0] + ' ' + cls[0] + ' ' + args[0]
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print("Provides description of a given command")
        return True

    def emptyline(self):
        """Empty line handler"""
        pass

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")
        return True

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program")
        return True

    def help_help(self):
        """Help for help command"""
        print("Help command to display available commands")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()

