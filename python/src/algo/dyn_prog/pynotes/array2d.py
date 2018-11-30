'''
Created on Jul 3, 2017

@author: zha970
'''

class Array2d(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        print("Array2d constructor")
    
    @staticmethod
    def create(m, n):
        A = [[0 for x in range(m)] for y in range(n)]
        return A

    @staticmethod
    def print2d(A):
        l = len(A)
        for i in range(l):
            print(A[i])

    # To declare a 2d array, the following two ways are different
    #     A = [[0] * l1] * l2
    # and
    #     A = [[0 for x in range(l1)] for y in range(l2)]
    # Conclusion:
    # 1. Using multiplication looks like it duplicates the reference
    # 2. Using "for" loop really creates new arrays

    def init2d_array_using_star(self):
        m = 3
        n = 4
        A = [ [0] * m ] * n
        Array2d.print2d(A)
        # If you change the first row, *ALL* rows will be changed

        print("Changing the first row ...")
        A[0][0] = 1
        Array2d.print2d(A)

        print("Changing the 2nd row ...")
        A[1][1] = 2
        Array2d.print2d(A)

    def init2d_array(self):
        m = 5
        n = 6
        A = [[0 for x in range(m)] for y in range(n)]
        Array2d.print2d(A)
        # If you change the first row, *ALL* rows will be changed

        print("Changing the first row ...")
        A[0][0] = 1
        Array2d.print2d(A)

        print("Changing the 2nd row ...")
        A[1][1] = 2
        Array2d.print2d(A)

if __name__ == "__main__":
    o = Array2d()
    o.init2d_array_using_star()
    o.init2d_array()

    A = Array2d.create(2, 3)
    Array2d.print2d(A)
    A[1][1] = 10
    Array2d.print2d(A)