class Methods(object):
    def imeth(self, x):     # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def smeth(x):           # Static: no instance passed
        print([x])

    @classmethod
    def cmeth(cls, x):      # Class: gets class, not instance
        print([cls, x])

print("Now instance method ...")
obj = Methods()
print(obj.imeth(1))
print(obj.imeth(2))

print("Now static method ...")
print(Methods.smeth(3))
print(obj.smeth(4))

print("Now class method ...")
print(Methods.cmeth(5))
print(obj.smeth(6))
