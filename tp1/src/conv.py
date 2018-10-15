# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:29:27 2018

@authors: kevin, yujia
"""

import sys
import time

# Path for product debugging
#"../testset/serie1/ex_4.1"#

ex_path1 = sys.argv[1] # Path of the first matrix
ex_path2 = sys.argv[2] # Path of the second matrix

def extractMatrix(flie_name):
    new_matrix = []
    
    with open(flie_name,'r') as file:
        for line in file:
            line = line.strip()
            if len(line) > 1:
               new_matrix.append([int(a) for a in line.split()])
    file.close()
    
    return new_matrix

def conv(ex_path1, ex_path2):
    matrix_A = []
    matrix_B = []
    matrix_A = extractMatrix(ex_path1)
    matrix_B = extractMatrix(ex_path2)
    
    # Sizes and types must be equals to perform a multiplication
    assert type(matrix_A) == list and type(matrix_B) == list
    assert len(matrix_A) == len(matrix_A[0]) == len(matrix_B) == len(matrix_B[0])
    
    # Start time count
    start_time = time.time()
    
    # matrix initialization
    w, h = len(matrix_A[0]), len(matrix_B[0]);
    matrix_C = [[0 for x in range(w)] for y in range(h)]
    	
    for i in range(len(matrix_A)):
       # iterate through columns of Y
       for j in range(len(matrix_B[0])):
           # iterate through rows of Y
           for k in range(len(matrix_B)):
               matrix_C[i][j] += matrix_A[i][k] * matrix_B[k][j]  
    
    # End time count
    global runtime
    end_time = time.time()
    runtime = end_time - start_time
    
    return matrix_C

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
matrix_C = conv(ex_path1, ex_path2)

# Call options (interface du laboratoire)
options = sys.argv[3:]
if '-p' in options: # Print result
    printMatrix(matrix_C)
if '-t' in options: # Print execution time
    print(runtime)
    