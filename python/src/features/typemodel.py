class C: pass
class D: pass

c, d = C(), D()

print(type(c), type(d))
print(c.__class__, d.__class__)
print(type(c) == type(d))


