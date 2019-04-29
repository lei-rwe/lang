from library import Base

class Derived(Base):
    def bar(self):
        print("Derived.bar")

if __name__ == '__main__':
    d = Derived()
    d.foo()