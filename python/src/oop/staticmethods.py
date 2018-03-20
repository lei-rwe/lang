class Spam:
    numInstances = 0
    def __init__(self):
        self.attr = 100
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print("Number of instances created: %s" % Spam.numInstances)

    @staticmethod
    def func1(self):
        print(self.attr)

a = Spam()
b = Spam()
c = Spam()

Spam.printNumInstances()
Spam.func1(c)