class C: # In Python 3.X
    def __getitem__(self, ix): # Indexing overload method
        print('C index')

class D(C):
    def __getitem__(self, ix): # Redefine to extend here
        print('D index')
        C.__getitem__(self, ix) # Traditional call form works
        super(D, self).__getitem__(ix) # Direct name calls work too
        super()[ix] # But operators do not! (__getattribute__)

X = C()
print(X[99])

X = D()
print(X[99])
