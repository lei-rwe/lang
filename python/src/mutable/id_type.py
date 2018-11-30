# https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747 2/

# Question: how to prove that int is immutable?
#    x = 10
#    x = x + 1     # This will change the id of x

''' Example 1 '''
x = "Holberton"
y = "Holberton"
print(id(x))
print(id(x))
print(x is y) # comparing the types'''

''' Example 2 '''
a = 50
print(type(a))
b = "Holberton"
print(type(b))

x = 10
print("id(x): ", id(x))
print("id(10): ", id(10))
x = x + 1
print("After x = x + 1, id(x): ", id(x))
print("After x = x + 1, id(x): ", id(11))

# Now, how to prove mutable objects are mutable?
l = [1, 21, 3]
print(id(l))

l.append("Append something")
print(id(l))


def updateList(list1):
    list1 += [10]

n = [5, 6]
print("id(n):", id(n))
updateList(n)
print(n) # [5, 6, 10]
print("After update, id(n):", id(n)) # 140312184155336

def updateNumber(n):
    print(id(n))
n += 10
b = 5
print("id(b):", id(b))
updateNumber(b)
print(b)
print("After updateNumber, id(b):", id(b))
