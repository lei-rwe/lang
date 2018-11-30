class properties(object):
    @property
    def age(self):
        print("property age")
        return self._age_

    @age.setter
    def age(self, v):
        print("set property age")
        self._age_ = v

if __name__ == '__main__':
    o = properties()
    o.age = 30
    print(o.age)
