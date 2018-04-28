class C1:
    def method_1(self):
        self.__X = 88
    def method_2(self):
        print("In class C1:", self.__X)
class C2:
    def method_a(self):
        self.__X = 99
    def method_b(self):
        print("In class C2:", self.__X)

class C3(C2,C1):
    pass

if __name__ == '__main__':
    a = C3()
    a.method_1()
    a.method_a()
    print(a.__dict__)
