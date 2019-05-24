# Purpose: how to update PART of a DataFrame based on the other DataFrame
# Google: To update a column in DataFrame based on column in the other DataFrame
# https://stackoverflow.com/questions/24768657/replace-column-values-based-on-anot
import numpy as np
import pandas as pd
import random

M = pd.DataFrame({'A': range(1, 5), 'B': range(100, 500, 100)})
N = pd.DataFrame({'B': [4, 5, 6], 'C': [7, 8, 9]})

# Partly update a given DataFrame from the other one.
# Should focus on locating the indexes.
# For the following two DataFrame, update M column Z, using N column C,
# based on M.X == N.B

M = pd.DataFrame({'X': range(10, 90, 10), 'Z': range(100, 900, 100)})
N = pd.DataFrame({'B': [40, 55, 60, 20, 38], 'C': range(-1, -6, -1)})

# Need to get the indices in M for the elements of N, w.r.t the columns X and B
# Hence, MANIPULATE the INDICES of M

M1=M['X']
M2=M1.reset_index()

A = N.merge(M2, left_on='B', right_on='X')
B = A.set_index('index').drop(['X', 'B'], axis=1)
B.columns = ['Z']

import pdb; pdb.set_trace()
M.update(B)

T = N.merge(M['X'].reset_index(), left_on='B', right_on='X').set_index('index')['C'].rename(columns={'C':'Z'})
