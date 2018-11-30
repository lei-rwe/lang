class Base:
    subclasses = []

    def __init_subclass__(cls, **kwargs):
        print('__init_subclass__ ->', cls)
        super().__init_subclass__(**kwargs)
        cls.subclasses.append(cls)

class C1(Base): # __init_subclass__ will be called here
    pass

class C2(Base): # __init_subclass__ will be called here
    pass


if __name__ == '__main__':
    # o1 = C1()
    print("Test")
