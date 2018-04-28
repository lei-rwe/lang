class MyClass:
    minstance = 0

    another_static_member = 100
    print another_static_member     # This will be printed ONLY once

    def __init__(self):
        print "MyClass::__init__"
        self.member = 10
        MyClass.minstance += 1

    @staticmethod
    def get_instance_count():
        return MyClass.minstance

if __name__ == "__main__":
    mylist = []
    for i in range(2):
        mylist.append(MyClass())

    print "Total instances created: ", MyClass.get_instance_count()
