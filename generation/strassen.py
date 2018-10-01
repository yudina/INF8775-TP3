# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:29:27 2018

@author: kevin
"""

import numpy as np
import sys
import os
import argparse
import time
import pandas as pd
import csv

#arg1 = sys.argv[1]
#arg2 = sys.argv[2]
aFile = open("ex1.1", 'r')
bFile = open("ex1.2", 'r')
global aN, bN # les exposants n
aN = int(aFile.readline())
bN = int(bFile.readline())
counter = 0

global times
times = []

def genMatrix(fileName, d):
    newMatrix = []
    
    with open(fileName,'r') as f1:
        for line in f1:
            line = line.strip()
            if len(line) > 1:
               newMatrix.append([int(a) for a in line.split()])
    return newMatrix
#    print(d)
#    datalines = inFile
#    newMatrix = []
#
#    for x in range(0,d):
#        dataline = datalines.readline().split()
#        for y in range(0,d):
#            yVals = list(map(float, dataline))
#
#        newMatrix.append(yVals)
#    return newMatrix

def partitionMatrix(matrix):
    length = len(matrix)
    if(length % 2 is not 0):
        stack = []
        for x in range(length + 1):
            stack.append(float(0))
        length += 1
        matrix = np.insert(matrix, len(matrix), values=0, axis=1)
        matrix = np.vstack([matrix, stack])
    d = (length // 2)
    matrix = matrix.reshape(length, length)
    completedPartition = [matrix[:d, :d], matrix[d:, :d], matrix[:d, d:], matrix[d:, d:]]
    return completedPartition

def strassen(mA, mB):
    n1 = len(mA) # nbr de col
    n2 = len(mB)
    global aN
    if(n1 and n2 <= aN): # hein ? faire un prodScal si la matrice est assez petite ?
        return (mA * mB)
    else:
        print(mA)
        A = partitionMatrix(mA)
        B = partitionMatrix(mB)
        mc = np.matrix([0 for i in range(len(mA))]for j in range(len(mB)))
        C = partitionMatrix(mc)


        a11 = np.array(A[0])
        a12 = np.array(A[2])
        a21 = np.array(A[1])
        a22 = np.array(A[3])

        b11 = np.array(B[0])
        b12 = np.array(B[2])
        b21 = np.array(B[1])
        b22 = np.array(B[3])

        mone = np.array(strassen((a11 + a22), (b11 + b22)))
        mtwo = np.array(strassen((a21 + a22), b11))
        mthree = np.array(strassen(a11, (b12 - b22)))
        mfour = np.array(strassen(a22, (b21 - b11)))
        mfive = np.array(strassen((a11 + a12), b22))
        msix = np.array(strassen((a21 - a11), (b11 + b12)))
        mseven = np.array(strassen((a12 - a22), (b21 + b22)))

        C[0] = np.array((mone + mfour - mfive + mseven))
        C[2] = np.array((mthree + mfive))
        C[1] = np.array((mtwo + mfour))
        C[3] = np.array((mone - mtwo + mthree + msix))

        return np.array(C)

if __name__ == "__main__":
    matrixA = genMatrix("ex1.1", aN)
    matrixB = genMatrix("ex1.2", bN)
    matrixA = np.matrix(matrixA)
    matrixB = np.matrix(matrixB)
    
    start_time = time.time()
    matrixC = strassen(matrixA, matrixB)
    runtime = time.time() - start_time
    times.append(runtime)
    
    listMatrixC = []
    lenA = len(matrixA)
    
    listMatrixC = [[matrixC.item(((lenA*i)+j)) for i in range(len(matrixA))]for j in range(len(matrixA))]

    print("listC =")
    print(listMatrixC)
    
    print(times)

csvfile = "outStrassen.csv"

#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for t in times:
        writer.writerow([t])  