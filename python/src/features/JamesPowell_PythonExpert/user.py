# How can you make sure your code fails anytime earlier than runtime
# if method foo() is not provided by Base class?
# You can check if "hasattr"

from library import Base

assert hasattr(Base, 'foo'), "You broke it, you fool!"

class Derived(Base):
    def bar(self):
        return self.foo()    # How to make sure foo() is in base()

    def imp_by_user(self):
        print('Derived.imp_by_user()')
        return 'Implementation an abstract method'

obj = Derived()
obj.bar()
obj.req()
