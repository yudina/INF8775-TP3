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

import os
import argparse
import time
import pandas as pd
import numpy as np

#file1 = sys.argv[1]
#file2 = sys.argv[2]
start_time = time.time()
def conv(ex1, ex2):  
    
    X = []
    Y = []
    
    with open(ex1,'r') as f1:
        for line in f1:
            line = line.strip()
            if len(line) > 1:
               X.append([int(a) for a in line.split()])
    print(X)

    with open(ex2,'r') as f2:
        for line in f2:
            line = line.strip()
            if len(line) > 1:
               Y.append([int(a) for a in line.split()])
    print(Y)

    w, h = len(X[0]), len(Y[0]);
    result = [[0 for x in range(w)] for y in range(h)] 
    	
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]  
    for r in result:
       print(r)      
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--ex1', default='ex1.1', type=str)
    parser.add_argument('--ex2', default='ex1.2', type=str)
    args = parser.parse_args() 
    
    conv(args.ex1, args.ex2)
    #conv('ex1.1', 'ex1.2')
    print("--- %s seconds ---" % (time.time() - start_time))