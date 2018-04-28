def factory(klass, *args, **kwargs):
    return klass(*args, **kwargs)

class spam:
    def doit(self, msg):
        print(msg)

class person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job

object1 = factory(spam)
object2 = factory(person, "John", "Engineer")
object3 = factory(person, "Tim", "Teacher")

object1.doit("Message ")
