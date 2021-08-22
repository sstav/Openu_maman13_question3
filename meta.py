# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Users:
    def __init__(self, name, profession):
        self.name = name
        self.profession = profession


class Engineers(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "מהנדסים"


class Technicians(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "טכנאים"


class Barber(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "ספרים"


class Politicians(Users):
    def __init__(self, name, profession):
        super().__init__(name, profession)

    def __str__(self):
        return "פוליטיקאים"

