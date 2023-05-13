#!/usr/bin/env python3
"""
Entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Empty line handler"""
        pass

    def help_quit(self):
        """Help for quit command"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """Help for EOF command"""
        print("EOF command to exit the program")

    def help_help(self):
        """Help for help command"""
        print("Help command to display available commands")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

