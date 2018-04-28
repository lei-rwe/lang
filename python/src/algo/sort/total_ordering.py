import functools

@functools.total_ordering
class Student:
    def __init__(self, fn, ln):
        self.firstname = fn
        self.lastname = ln

    def __eq__(self, other):
        return ( (self.lastname.lower(), self.firstname.lower()) == 
                 (other.lastname.lower(), other.firstname.lower()) )

    def __lt__(self, other):
        return ( (self.lastname.lower(), self.firstname.lower()) <
                 (other.lastname.lower(), other.firstname.lower()) )

john = Student("John", "Doe")
amy  = Student("Amy", "Maple")


print(john <= amy)
print(john >= amy)
