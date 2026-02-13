class person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(person):
  pass

x = Student("Mike", "Olsen")
x.printname()