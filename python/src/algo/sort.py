from operator import itemgetter, attrgetter, methodcaller
class Student:
    def __init__(self, name, grade, age):
            self.name = name
            self.grade = grade
            self.age = age
    def __repr__(self):
            return repr((self.name, self.grade, self.age))
    def weighted_grade(self):
            return 'CBA'.index(self.grade) / float(self.age)

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

s = sorted(student_objects, key=attrgetter('age'))     # sort on secondary key
print s

s = sorted(s, key=attrgetter('grade'), reverse=False)  # now sort on primary key, descending
print s

