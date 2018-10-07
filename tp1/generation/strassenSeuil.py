# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:46:48 2018

@author: kevin
"""

from optparse import OptionParser
from math import ceil, log
import time
import csv

global times
times = []

def extractMatrix(fileName):
    newMatrix = []
    
    with open(fileName,'r') as f1:
        for line in f1:
            line = line.strip()
            if len(line) > 1:
               newMatrix.append([int(a) for a in line.split()])
    return newMatrix

def read(filename):
    lines = open(filename, 'r').read().splitlines()
    A = []
    B = []
    matrix = A
    for line in lines:
        if line != "":
            matrix.append(map(int, line.split("\t")))
        else:
            matrix = B
    return A, B

def conventionnalProduct(matrixA, matrixB):
#    n = len(A)
#    C = [[0 for i in xrange(n)] for j in xrange(n)]
#    for i in xrange(n):
#        for k in xrange(n):
#            for j in xrange(n):
#                C[i][j] += A[i][k] * B[k][j]
#    return C
    
    
    # matrix initialization
    w, h = len(matrixA[0]), len(matrixB[0]);
    matrixC = [[0 for x in range(w)] for y in range(h)]
    
    for i in range(len(matrixA)):
       # iterate through columns of Y
       for j in range(len(matrixB[0])):
           # iterate through rows of Y
           for k in range(len(matrixB)):
               matrixC[i][j] += matrixA[i][k] * matrixB[k][j]  
    return matrixC

def add(matrixA, matrixB):
    n = len(matrixA)
    matrixC = [[0 for j in range(0, n)] for i in range(0, n)]
    
    for i in range(0, n):
        for j in range(0, n):
            matrixC[i][j] = matrixA[i][j] + matrixB[i][j]
    return matrixC

def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = A[i][j] - B[i][j]
    return C

def strassen(A, B):
    """ 
        Implementation of the strassen algorithm.
    """
    n = len(A)

    if n <= LEAF_SIZE:
        return conventionnalProduct(A, B)
    else:
        # initializing the new sub-matrices
        newSize = int(n/2)
        a11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        a22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

        b11 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b12 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b21 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        b22 = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

        aResult = [[0 for j in range(0, newSize)] for i in range(0, newSize)]
        bResult = [[0 for j in range(0, newSize)] for i in range(0, newSize)]

        # dividing the matrices in 4 sub-matrices:
        for i in range(0, newSize):
            for j in range(0, newSize):
                a11[i][j] = A[i][j]            # top left
                a12[i][j] = A[i][j + newSize]    # top right
                a21[i][j] = A[i + newSize][j]    # bottom left
                a22[i][j] = A[i + newSize][j + newSize] # bottom right

                b11[i][j] = B[i][j]            # top left
                b12[i][j] = B[i][j + newSize]    # top right
                b21[i][j] = B[i + newSize][j]    # bottom left
                b22[i][j] = B[i + newSize][j + newSize] # bottom right

        # Calculating p1 to p7:
        aResult = add(a11, a22)
        bResult = add(b11, b22)
        p1 = strassen(aResult, bResult) # p1 = (a11+a22) * (b11+b22)

        aResult = add(a21, a22)      # a21 + a22
        p2 = strassen(aResult, b11)  # p2 = (a21+a22) * (b11)

        bResult = subtract(b12, b22) # b12 - b22
        p3 = strassen(a11, bResult)  # p3 = (a11) * (b12 - b22)

        bResult = subtract(b21, b11) # b21 - b11
        p4 =strassen(a22, bResult)   # p4 = (a22) * (b21 - b11)

        aResult = add(a11, a12)      # a11 + a12
        p5 = strassen(aResult, b22)  # p5 = (a11+a12) * (b22)   

        aResult = subtract(a21, a11) # a21 - a11
        bResult = add(b11, b12)      # b11 + b12
        p6 = strassen(aResult, bResult) # p6 = (a21-a11) * (b11+b12)

        aResult = subtract(a12, a22) # a12 - a22
        bResult = add(b21, b22)      # b21 + b22
        p7 = strassen(aResult, bResult) # p7 = (a12-a22) * (b21+b22)

        # calculating c21, c21, c11 e c22:
        c12 = add(p3, p5) # c12 = p3 + p5
        c21 = add(p2, p4)  # c21 = p2 + p4

        aResult = add(p1, p4) # p1 + p4
        bResult = add(aResult, p7) # p1 + p4 + p7
        c11 = subtract(bResult, p5) # c11 = p1 + p4 - p5 + p7

        aResult = add(p1, p3) # p1 + p3
        bResult = add(aResult, p6) # p1 + p3 + p6
        c22 = subtract(bResult, p2) # c22 = p1 + p3 - p2 + p6

        # Grouping the results obtained in a single matrix:
        C = [[0 for j in range(0, n)] for i in range(0, n)]
        for i in range(0, newSize):
            for j in range(0, newSize):
                C[i][j] = c11[i][j]
                C[i][j + newSize] = c12[i][j]
                C[i + newSize][j] = c21[i][j]
                C[i + newSize][j + newSize] = c22[i][j]
        return C

def runStrassen(filenameA, filenameB):
    A = extractMatrix(filenameA)
    B = extractMatrix(filenameB)
    assert type(A) == list and type(B) == list
    assert len(A) == len(A[0]) == len(B) == len(B[0])

    # Make the matrices bigger so that you can apply the strassen
    # algorithm recursively without having to deal with odd
    # matrix sizes
    nextPowerOfTwo = lambda n: 2**int(ceil(log(n,2)))
    n = len(A)
    m = nextPowerOfTwo(n)
    APrep = [[0 for i in range(m)] for j in range(m)]
    BPrep = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            APrep[i][j] = A[i][j]
            BPrep[i][j] = B[i][j]
    CPrep = strassen(APrep, BPrep)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = CPrep[i][j]
    print("result value is :")
    print(C)
    return C

if __name__ == "__main__":
    
    LEAF_SIZE = 1
    
    print("started strassen")
    main_start_time = time.time()
    runStrassen("ex1.1","ex1.2")
#    runStrassen("ex1.1","ex1.3")
#    runStrassen("ex1.1","ex1.4")
#    runStrassen("ex1.1","ex1.5")
#    runStrassen("ex1.2","ex1.3")
#    runStrassen("ex1.2","ex1.4")
#    runStrassen("ex1.2","ex1.5")
#    runStrassen("ex1.3","ex1.4")
#    runStrassen("ex1.3","ex1.5")
#    runStrassen("ex1.4","ex1.5")
#    
#    runStrassen("ex2.1","ex2.2")
#    runStrassen("ex2.1","ex2.3")
#    runStrassen("ex2.1","ex2.4")
#    runStrassen("ex2.1","ex2.5")
#    runStrassen("ex2.2","ex2.3")
#    runStrassen("ex2.2","ex2.4")
#    runStrassen("ex2.2","ex2.5")
#    runStrassen("ex2.3","ex2.4")
#    runStrassen("ex2.3","ex2.5")
#    runStrassen("ex2.4","ex2.5")
#    
#    runStrassen("ex3.1","ex3.2")
#    runStrassen("ex3.1","ex3.3")
#    runStrassen("ex3.1","ex3.4")
#    runStrassen("ex3.1","ex3.5")
#    runStrassen("ex3.2","ex3.3")
#    runStrassen("ex3.2","ex3.4")
#    runStrassen("ex3.2","ex3.5")
#    runStrassen("ex3.3","ex3.4")
#    runStrassen("ex3.3","ex3.5")
#    runStrassen("ex3.4","ex3.5")
#    
#    runStrassen("ex4.1","ex4.2")
#    runStrassen("ex4.1","ex4.3")
#    runStrassen("ex4.1","ex4.4")
#    runStrassen("ex4.1","ex4.5")
#    runStrassen("ex4.2","ex4.3")
#    runStrassen("ex4.2","ex4.4")
#    runStrassen("ex4.2","ex4.5")
#    runStrassen("ex4.3","ex4.4")
#    runStrassen("ex4.3","ex4.5")
#    runStrassen("ex4.4","ex4.5")
#    
#    runStrassen("ex5.1","ex5.2")
#    runStrassen("ex5.1","ex5.3")
#    runStrassen("ex5.1","ex5.4")
#    runStrassen("ex5.1","ex5.5")
#    runStrassen("ex5.2","ex5.3")
#    runStrassen("ex5.2","ex5.4")
#    runStrassen("ex5.2","ex5.5")
#    runStrassen("ex5.3","ex5.4")
#    runStrassen("ex5.3","ex5.5")
#    runStrassen("ex5.4","ex5.5")
    
    main_runtime = time.time() - main_start_time
    times.append(main_runtime)
    
    print(times)
    print("main_runtime : ")
    print(main_runtime)

csvfile = "outStrassen.csv"

#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for t in times:
        writer.writerow([t])  
    
#    parser = OptionParser()
#    parser.add_option("-i", dest="filename", default="2000.in",
#         help="input file with two matrices", metavar="FILE")
#    parser.add_option("-l", dest="LEAF_SIZE", default="8",
#         help="when do you start using ikj", metavar="LEAF_SIZE")
#    (options, args) = parser.parse_args()
#
#    LEAF_SIZE = options.LEAF_SIZE
#    A, B = read(options.filename)
#
#    C = strassen(A, B)
#    print(C)

