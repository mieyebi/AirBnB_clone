#!/usr/bin/python3
"""simple command interpreter to manipulate objects"""


import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models import storage
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """cmd custom class"""

    prompt = "(hbnb) "
    models = ["BaseModel", "User", "State", "City", "Amenity",
              "Place", "Review"]

    def do_EOF(self, arg):
        """quit interpreter"""
        return True

    def do_quit(self, arg):
        """quit interpreter"""
        return True

    def emptyline(self):
        """don't do anything"""
        pass

    def precmd(self, line):
        """parses line to appropriate commands"""
        if not line:
            return line
        if line[-1] == ")":
            line_split_by_dot = line.split(".")
            if len(line_split_by_dot) < 2:
                self.default(line)
                return ""
            if line_split_by_dot[1] == "all()":
                line = "{} {}".format(line_split_by_dot[1].strip("()"),
                                      line_split_by_dot[0])
                return line

            if line_split_by_dot[1] == "count()":
                cls = line_split_by_dot[0]
                i = 0
                for key in storage.all():
                    if key.startswith(cls):
                        i += 1
                print(i)
                return ""
            if line_split_by_dot[1].startswith("show("):
                # do_show syntax: show class_name id
                # line_dot_split = [class, show(id)]
                cls = line_split_by_dot[0]
                cmd = line_split_by_dot[1].split("(")[0]
                # id_ = line_split_by_dot[1].strip("show()")
                id_ = line_split_by_dot[1][5:].strip('")"')
                id_ = id_.strip("'")
                line = "{} {} {}".format(cmd, cls, id_)
                return line
            if line_split_by_dot[1].startswith("destroy("):
                # do_destroy syntax: destroy class_name id
                # line_dot_split = [class, destroy(id)]
                cls = line_split_by_dot[0]
                cmd = line_split_by_dot[1].split("(")[0]
                # id_ = line_split_by_dot[1].strip("destroy()")
                id_ = line_split_by_dot[1][8:].strip('")"')
                id_ = id_.strip("'")
                line = "{} {} {}".format(cmd, cls, id_)
                return line
            if line_split_by_dot[1].startswith("update("):
                # do_update syntax: update class_name id attribute val
                # line_dot_split = [class, update(id, attr, val)]
                # or = [class, update(id, dict)]
                cls = line_split_by_dot[0]
                cmd = line_split_by_dot[1].split("(")[0]
                # id_and_args = line_split_by_dot[1].strip("update()")
                id_and_args = line_split_by_dot[1][7:].strip(")")
                # id_and_args = id, dict
                id_ = ""
                idx = 0
                while id_and_args[idx] != "," and idx < len(id_and_args):
                    id_ += id_and_args[idx]
                    idx += 1
                id_ = id_.strip('"')
                id_ = id_.strip("'")
                idx += 1
                args = id_and_args[idx:]
                args = args.strip(" '")
                args = args.strip('"')
                # id_and_args_list = id_and_args.split(",")
                # id_ = id_and_args_list[0].strip('"')
                # args = id_and_args_list[1]
                line = "{} {} {} {}".format(cmd, cls, id_, args)
                return line

        return line

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if arg:
            args = arg.split()
            if args[0] not in self.models:
                print("** class doesn't exist **")
            else:
                if args[0] == "BaseModel":
                    inst = BaseModel()
                elif args[0] == "User":
                    inst = User()
                elif args[0] == "State":
                    inst = State()
                elif args[0] == "City":
                    inst = City()
                elif args[0] == "Amenity":
                    inst = Amenity()
                elif args[0] == "Place":
                    inst = Place()
                elif args[0] == "Review":
                    inst = Review()
                inst.save()
                print(inst.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """prints the string representation of an instance \
based on the class name and its id"""
        if arg:
            args = arg.split()
            if args[0] not in self.models:
                print("** class doesn't exist **")
                return False
            if len(args) < 2:
                print("** instance id missing **")
                return False
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return False
            inst = storage.all()[key]
            print(inst)
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg:
            args = arg.split()
            if args[0] not in self.models:
                print("** class doesn't exist **")
                return False
            if len(args) < 2:
                print("** instance id missing **")
                return False
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return False
            del storage.all()[key]
            storage.save()
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = storage.all()
        lst = []
        if not objects:
            print(lst)
            return False
        for item in objects:
            lst.append(str(objects[item]))
        if not arg:
            print(lst)
            return False
        args = arg.split()
        if args[0] not in self.models:
            print("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                BaseModel_list = []
                for item in lst:
                    if item.startswith("[BaseModel]"):
                        BaseModel_list.append(item)
                print(BaseModel_list)
            elif args[0] == "User":
                User_list = []
                for item in lst:
                    if item.startswith("[User]"):
                        User_list.append(item)
                print(User_list)
            elif args[0] == "State":
                State_list = []
                for item in lst:
                    if item.startswith("[State]"):
                        State_list.append(item)
                print(State_list)
            elif args[0] == "City":
                City_list = []
                for item in lst:
                    if item.startswith("[City]"):
                        City_list.append(item)
                print(City_list)
            elif args[0] == "Amenity":
                Amenity_list = []
                for item in lst:
                    if item.startswith("[Amenity]"):
                        Amenity_list.append(item)
                print(Amenity_list)
            elif args[0] == "Place":
                Place_list = []
                for item in lst:
                    if item.startswith("[Place]"):
                        Place_list.append(item)
                print(Place_list)
            elif args[0] == "Review":
                Review_list = []
                for item in lst:
                    if item.startswith("[Review]"):
                        Review_list.append(item)
                print(Review_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg:
            # update syntax: update class id attr val
            args = arg.split()
            if len(args) > 2:
                if args[2].startswith("{"):
                    ending = ''.join(args[2:])
                    ending_ = ''
                    for char in ending:
                        if char == "'":
                            ending_ += '"'
                        else:
                            ending_ += char
                    args[2] = ending_
                    if len(args) > 3:
                        args[3:] = []
            if args[0] not in self.models:
                print("** class doesn't exist **")
                return False
            if len(args) < 2:
                print("** instance id missing **")
                return False
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return False
            if len(args) < 3:
                print("** attribute name missing **")
                return False
            if len(args) == 3:
                import json
                try:
                    dct = json.loads(args[2])
                    if isinstance(dct, dict):
                        objects_dct = storage.all()
                        for obj_id in objects_dct:
                            if key == obj_id:
                                obj = objects_dct[key]
                                break
                        for item in dct:
                            obj.__dict__[item] = dct[item]
                        obj.save()
                        return False
                except Exception as e:
                    print("** value missing **")
                    return False
            if len(args) < 4:
                print("** value missing **")
                return False
            objects_dct = storage.all()
            for obj_id in objects_dct:
                if key == obj_id:
                    obj = objects_dct[key]
                    break
            attr_name = args[2]
            value = args[3]
            try:
                if isinstance(obj.__dict__[attr_name], int):
                    obj.__dict__[attr_name] = int(value)
                else:
                    obj.__dict__[attr_name] = value
            except Exception:
                obj.__dict__[attr_name] = value
            obj.save()
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
