import numpy as np
import pandas as pd

############################################
######        Series         ###############

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = dict(zip(labels, my_data))

s1 = pd.Series(data = my_data)
print(s1)
s2 = pd.Series(data = my_data, index=labels)
print(s2)
s3 = pd.Series(d)
print(s3)

s = pd.Series(data = [sum, print, len])
print(s)

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)

print('ser1["USA"]=', ser1["USA"])

print(ser1 + ser2)

############################################
######        DataFrame         ############

from numpy.random import randn
np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)

print('type(DataFrame)=',type(df['W']))
print(df[['W', 'Z']])

df['new'] = df['W'] + df['Z']
print(df)

df.drop('new', axis=1, inplace=True)

### ROWS
print(df.loc['A'])
print(df.iloc[3])
print(df.loc['A', 'Z'])
print(df.shape)
print(df.loc[['A','B'],['W','Y']])

# Conditional selection
print(df[df>0])
print(df[df['W']>0])
print(df[df['W']>0][['Y','Z']])

bser = df['W'] > 0
result = df[bser]
cols = ['Y', 'X']
print(result[cols])

print(df[(df['W']>0) & (df['Y']>1)])

df['States'] = 'CA NY WY OR CO'.split()
df.set_index('States')
df.reset_index()

############################################
######        Index Levels         #########

outside = ['G1'] * 3 + ['G2'] * 3
inside = ['1','2','3'] * 2
hier_index = tuple(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2), hier_index, ['A','B'])
print(df.loc['G1'])
df.index.names = ['Groups', 'Num']
print(df)

# Cross Section
print(df.xs('1', level='Num'))
import pdb; pdb.set_trace()
