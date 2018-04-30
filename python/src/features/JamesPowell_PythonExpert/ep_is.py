class Shape:
    def __init_subclass__(cls, default_name, **kwargs):
        super().__init_subclass__(**kwargs)
        print(f"Called __init_subclass({cls}, {default_name})")
        cls.default_name = default_name

        assert hasattr(cls, "foo"), "subclass does not define foo() method"

class Square(Shape, default_name="Square"):
    default_name = "Rectangle"
    print("Set name to Rectangle")

    def __init__(self):
        print('Square.__init__')

    def bar(self):
        pass

square = Square()
print(square.default_name)