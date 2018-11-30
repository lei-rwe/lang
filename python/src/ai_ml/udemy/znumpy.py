import numpy as np

my_list = [1, 2, 3]
np_list = np.array(my_list)

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np_matrix = np.array(my_matrix)

nprg_1 = np.arange(30, 54)
nprg_2 = nprg_1.reshape(4, 6)

z = np.zeros( (3, 3, 3) )
o = np.ones( (4, 5) )
I = np.eye(4)

# Return evenly spaced numbers over a specified interval.
line = np.linspace(0, 1, 10)

# Create random number arrays
# rand - uniform distribution
# randn - standard normal distribution
# randint - discrete uniform distribution

rdarray = np.random.rand(5)
print("np.random.rand(5)=", rdarray)
rdm = np.random.rand(5, 5)
print("np.random.rand(5,5)=", rdm)

rdn1 = np.random.randn(5)
print(rdn1)
rdn2 = np.random.randn(3,3)
print(rdn2)

rdi1 = np.random.randint(10, 50, 6)
print(rdi1)

ranarr = np.random.randint(0,50,10)

############################################
# NumPy Indexing and Selection

arr = np.arange(0, 11)
print("sample numpy array: ", arr)
print("arr[5]=", arr[5])
print("arr[3:6]=", arr[3:6])
print("arr[:4]=", arr[:4])
print("arr[7:]=", arr[7:])

# Broadcasting
arr[0:4] = 100
print(arr)

# By default array will NOT be copied
arr = np.arange(0, 11)
s = arr[2:5]
s[:] = 50
print(s)
print(arr)

# You have to explicitly copy
arr = np.arange(0, 11)
arr_copy = arr.copy()

# Indexing 2D Arrays
arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print("arr_2d=", arr_2d)
print("row: arr_2d[1]=", arr_2d[1])
print("arr_2d[1,2]=", arr_2d[1,2])
print("arr_2d[0:2,1:3]=", arr_2d[0:2,1:3])
print("column: arr_2d[:,1:2]=", arr_2d[:,1:2])
print("column to row: arr_2d[:,1]=", arr_2d[:,1])

# Selection
arr = np.arange(0, 11)
bool_arr = arr > 3
print(bool_arr)
print(arr[bool_arr])
print('arr[arr > 5] = ', arr[arr > 5])

############################################
# Array Operations

arr = np.arange(1, 10)
print("arr + arr = ", arr + arr)
print("arr - arr = ", arr - arr)
print("arr * arr = ", arr * arr)
print("arr / arr = ", arr / arr)
print("arr ** 2 = ", arr ** 2)
print("1 / arr = ", 1 / arr)
print("3 + arr = ", 3 + arr)
print("np.sqrt(arr)= ", np.sqrt(arr))
print("np.sin(arr)= ", np.sin(arr))
print("np.log(arr)= ", np.log(arr))
print("np.exp(arr)= ", np.exp(arr))
print("np.max(arr)= ", np.max(arr))
print("np.min(arr)= ", np.min(arr))
print("np.median(arr)= ", np.median(arr))

# From Exercies
mat = np.arange(1, 26).reshape(5,5 )
print(mat)

print("mat[2:,1:] = ", mat[2:,1:])
print("mat[3,4] = ", mat[3,4])

print("mat[0:3,1] = ", mat[0:3,1])       # This is different with the following one
print("mat[0:3,1:2] = ", mat[0:3,1:2])

print("mat[4] = ", mat[4])
print("mat[3:] = ", mat[3:])

print("np.sum(mat)=", np.sum(mat))
print("np.mean(mat)=", np.mean(mat))
print("np.std(mat)=", np.std(mat))

# Get the sum of all the columns in mat
print("np.sum(mat, axis=0)=", np.sum(mat, axis=0))
print("np.sum(mat, axis=1)=", np.sum(mat, axis=1))
