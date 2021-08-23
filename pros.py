# Standard import

class Users:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


# Professions Types:
class Engineers(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "מהנדסים"


class Technician(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "טכנאים"


class Barber(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "ספרים"


class Politician(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "פוליטיקאים"


# Types Of Engineers:
# Electrical:
class Electrical(Engineers):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return super().__str__() + ": " + "חשמל"


# Computers:
class Computers(Engineers):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return super().__str__() + ": " + "מחשבים"


# Machines:
class Machines(Engineers):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return super().__str__() + ": " + "מכונות"


# Helpers Functions:
def factory(_new_class, _base_class, _new_method, _new_attr):
    gen_class = type(_new_class, (Users,),
                     {
                         _new_method: lambda self: print("Self: " + self + " Method "),
                         _new_attr: _base_class
                     })

    return gen_class


# Main Program:

if __name__ == "__main__":
    new_class = input("Please enter the name of new class:")
    base_class = input("Please enter name of base class (blank if none):")
    new_method = input("Please enter name of new method for class Student:")
    new_attr = input("Please enter name of new attribute for class Student:")

    generate_new_class = factory(new_class, base_class, new_method, new_attr)

    print("Class " + new_class + " created with base class: " + str(base_class))
    print("Class __name__ is: " + generate_new_class.__name__)
    print("Class __dict__ is: " + str(generate_new_class.__dict__))
