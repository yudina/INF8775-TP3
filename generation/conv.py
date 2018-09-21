# Program to multiply two matrices using nested loops

# 3x3 matrix
# X = [[12,7,3],
    # [4 ,5,6],
    # [7 ,8,9]]
# 3x4 matrix
# Y = [[5,8,1,2],
    # [6,7,3,0],
    # [4,5,9,1]]
# result is 3x4

import sys
import datetime
import pandas as pd
import numpy as np

file1 = sys.argv[1]
file2 = sys.argv[2]

X = []
with open('file1','r') as f:
    for line in f:
        X.append(line.split())
data = pd.DataFrame(X,columns = ['row','column','value'])
data_ind = data.set_index(['row','column']).unstack('column')
np.array(data_ind.values,dtype=float)

Y = []
with open('file2','r') as f:
    for line in f:
        Y.append(line.split())
data = pd.DataFrame(Y,columns = ['row','column','value'])
data_ind = data.set_index(['row','column']).unstack('column')
np.array(data_ind.values,dtype=float)

result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
	
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
