# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 17:29:27 2018

@authors: kevin, yujia
"""

import sys
import time
import csv

global times
times = []

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

def printMatrix(matrix):
    # Obtain the N
    file = open(ex_path1, 'r')
    N = int(file.readline())
    file.close()
    
    # Output of the requested format
    print(N)
    for line in matrix:
        print("\t".join(map(str,line)))

def conv(ex_path1, ex_path2):
    matrixA = []
    matrixB = []
    matrixA = extractMatrix(ex_path1)
    matrixB = extractMatrix(ex_path2)
    
    start_time = time.time()
    
    # matrix initialization
    w, h = len(matrixA[0]), len(matrixB[0]);
    result = [[0 for x in range(w)] for y in range(h)]
    	
    for i in range(len(matrixA)):
       # iterate through columns of Y
       for j in range(len(matrixB[0])):
           # iterate through rows of Y
           for k in range(len(matrixB)):
               result[i][j] += matrixA[i][k] * matrixB[k][j]  
    
    global runtime
    end_time = time.time()
    runtime = end_time - start_time
    #times.append(runtime)
    return result
    #print("--- %s seconds ---" % (time.time() - start_time)) 
    
# Run the conventionnal algorithm
result = conv(ex_path1, ex_path2)

# Call options (interface du laboratoire)
options = sys.argv[3:]
if '-p' in options: # On imprime la matrice résultat
    printMatrix(result)
    #print("2\n1\t2\t3\t4\n5\t6\t7\t8\n9\t10\t11\t12\n13\t14\t15\t16") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print(runtime) # Données bidon, mais output du bon format demandé
    
#if __name__ == "__main__":
      
#    conv("ex1.1", "ex1.2")
#    conv("ex1.1", "ex1.3")
#    conv("ex1.1", "ex1.4")
#    conv("ex1.1", "ex1.5")
#    conv("ex1.2", "ex1.3")
#    conv("ex1.2", "ex1.4")
#    conv("ex1.2", "ex1.5")
#    conv("ex1.3", "ex1.4")
#    conv("ex1.3", "ex1.5")
#    conv("ex1.4", "ex1.5")
#    
#    conv("ex2.1", "ex2.2")
#    conv("ex2.1", "ex2.3")
#    conv("ex2.1", "ex2.4")
#    conv("ex2.1", "ex2.5")
#    conv("ex2.2", "ex2.3")
#    conv("ex2.2", "ex2.4")
#    conv("ex2.2", "ex2.5")
#    conv("ex2.3", "ex2.4")
#    conv("ex2.3", "ex2.5")
#    conv("ex2.4", "ex2.5")
#    
#    conv("ex3.1", "ex3.2")
#    conv("ex3.1", "ex3.3")
#    conv("ex3.1", "ex3.4")
#    conv("ex3.1", "ex3.5")
#    conv("ex3.2", "ex3.3")
#    conv("ex3.2", "ex3.4")
#    conv("ex3.2", "ex3.5")
#    conv("ex3.3", "ex3.4")
#    conv("ex3.3", "ex3.5")
#    conv("ex3.4", "ex3.5")
#    
#    conv("ex4.1", "ex4.2")
#    conv("ex4.1", "ex4.3")
#    conv("ex4.1", "ex4.4")
#    conv("ex4.1", "ex4.5")
#    conv("ex4.2", "ex4.3")
#    conv("ex4.2", "ex4.4")
#    conv("ex4.2", "ex4.5")
#    conv("ex4.3", "ex4.4")
#    conv("ex4.3", "ex4.5")
#    conv("ex4.4", "ex4.5")
#    
#    conv("ex5.1", "ex5.2")
#    conv("ex5.1", "ex5.3")
#    conv("ex5.1", "ex5.4")
#    conv("ex5.1", "ex5.5")
#    conv("ex5.2", "ex5.3")
#    conv("ex5.2", "ex5.4")
#    conv("ex5.2", "ex5.5")
#    conv("ex5.3", "ex5.4")
#    conv("ex5.3", "ex5.5")
#    conv("ex5.4", "ex5.5")
    
#    print("times")
#    print(times)
    
#csvfile = "outConv.csv"

#Assuming res is a flat list
#with open(csvfile, "w") as output:
#    writer = csv.writer(output, lineterminator='\n')
#    for t in times:
#        writer.writerow([t])    