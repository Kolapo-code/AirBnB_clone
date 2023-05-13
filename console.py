#!/usr/bin/python3
"""
    Entry point of the command interpreter
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    Implementation of the command interpreter for the HBNB project
    """

    prompt = "(hbnb) "
    valid_models = models.all_classes()

    def emptyline(self):
        """
        Method called when an empty line is entered in response to the prompt
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        model_name = args[0]
        if model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return

        instance = models.storage.create(model_name)
        models.storage.save()
        print(instance.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name and id
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        model_name = args[0]
        if model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = model_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        print(models.storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        model_name = args[0]
        if model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = model_name + "." + instance_id
        if key not in models.storage.all():
            print("** no instance found **")
            return

        models.storage.delete(models.storage.all()[key])
        models.storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or not on the class name
        """
        args = line.split()
        if args and args[0] not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return

        objects = [str(obj) for obj in models.storage.all().values()]
        if args:
            objects = [obj for obj in objects if obj.startswith("[{}]".format(args[0]))]
        print(objects)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or updating attribute
        """
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        model_name = args[0]
        if model_name not in HBNBCommand.valid_models:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = model_name + "." + instance_id


