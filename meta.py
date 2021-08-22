# Standard import
import importlib


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
def factory(classname, name, profession):
    # Get class from globals and create an instance
    m = globals()[classname]("234", "234")
    # Get the function (from the instance) that we need to call
    func = getattr(m,"234","234")
    # Return function
    return func()

#Main Program:


if __name__ == "__main__":
    while_quit = True
    while while_quit:
        new_class = input("Please enter the name of new class:")
        base_class = input("Please enter name of base class (blank if none):")
        new_method = input("Please enter name of new method for class Student:")
        new_attr = input("Please enter name of new attribute for class Student:")

        res = factory(res, 2323, 2323)
        print(res)



