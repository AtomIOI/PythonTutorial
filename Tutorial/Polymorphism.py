class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printinfo(self):
        return self.firstname + " " + self.lastname


class Doctor(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

    def printinfo(self):
        return "Dr." + self.firstname + " " + self.lastname



