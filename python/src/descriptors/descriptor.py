from weakref import WeakKeyDictionary
 
class Price(object):
    def __init__(self):
        self.default = 0
        self.values = WeakKeyDictionary()
 
    def __get__(self, instance, owner):
        print("In Price.__get__")
        return self.values.get(instance, self.default)
 
    def __set__(self, instance, value):
        print("In Price.__set__")
        if value < 0 or value > 100:
            raise ValueError("Price must be between 0 and 100.")
        self.values[instance] = value
 
    def __delete__(self, instance):
        del self.values[instance]

class Book(object):
    price = Price()
 
    def __init__(self, author, title, price):
        self.author = author
        self.title = title
        self.price = price
 
    def __str__(self):
        return "{0} - {1}".format(self.author, self.title)

if __name__ == '__main__':
    b = Book("William Faulkner", "The Sound and the Fury", 12)
    print(b.price)