# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:29:27 2018

@authors: kevin, yujia
"""

import sys
import time

"../testset/serie1/ex_4.1"#
ex_path1 = sys.argv[1] # Path of the first matrix
ex_path2 = sys.argv[2] # Path of the second matrix

def extractMatrix(fileName):
    newMatrix = []
    
    with open(fileName,'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > 1:
               newMatrix.append([int(a) for a in line.split()])
    file.close()
    
    return newMatrix

def conv(ex_path1, ex_path2):
    matrixA = []
    matrixB = []
    matrixA = extractMatrix(ex_path1)
    matrixB = extractMatrix(ex_path2)
    
    # Sizes and types must be equals to perform a multiplication
    assert type(matrixA) == list and type(matrixB) == list
    assert len(matrixA) == len(matrixA[0]) == len(matrixB) == len(matrixB[0])
    
    # Start time count
    start_time = time.time()
    
    # matrix initialization
    w, h = len(matrixA[0]), len(matrixB[0]);
    matrixC = [[0 for x in range(w)] for y in range(h)]
    	
    for i in range(len(matrixA)):
       # iterate through columns of Y
       for j in range(len(matrixB[0])):
           # iterate through rows of Y
           for k in range(len(matrixB)):
               matrixC[i][j] += matrixA[i][k] * matrixB[k][j]  
    
    # End time count
    global runtime
    end_time = time.time()
    runtime = end_time - start_time
    
    return matrixC

def printMatrix(matrix):
    # Obtain the N
    file = open(ex_path1, 'r')
    N = int(file.readline())
    file.close()
    
    # Output of the requested format
    print(N)
    for line in matrix:
        print("\t".join(map(str,line)))
# Run the conventionnal algorithm
matrixC = conv(ex_path1, ex_path2)

# Call options (interface du laboratoire)
options = sys.argv[3:]
if '-p' in options: # Print result
    printMatrix(matrixC)
if '-t' in options: # Print execution time
    print(runtime)
    