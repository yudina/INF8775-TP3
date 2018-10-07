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

def conv(matrixAName, matrixBName):

    matrixA = []
    matrixB = []
    matrixA = extractMatrix(matrixAName)
    matrixB = extractMatrix(matrixBName)
    
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
#    for r in result:
#       print(r) 
       
    runtime = time.time() - start_time
    times.append(runtime)
    #print("--- %s seconds ---" % (time.time() - start_time)) #TO DO: write to CSV the time taken to run program
    
if __name__ == "__main__":
      
    conv("ex1.1", "ex1.2")
    conv("ex1.1", "ex1.3")
    conv("ex1.1", "ex1.4")
    conv("ex1.1", "ex1.5")
    conv("ex1.2", "ex1.3")
    conv("ex1.2", "ex1.4")
    conv("ex1.2", "ex1.5")
    conv("ex1.3", "ex1.4")
    conv("ex1.3", "ex1.5")
    conv("ex1.4", "ex1.5")
    
    conv("ex2.1", "ex2.2")
    conv("ex2.1", "ex2.3")
    conv("ex2.1", "ex2.4")
    conv("ex2.1", "ex2.5")
    conv("ex2.2", "ex2.3")
    conv("ex2.2", "ex2.4")
    conv("ex2.2", "ex2.5")
    conv("ex2.3", "ex2.4")
    conv("ex2.3", "ex2.5")
    conv("ex2.4", "ex2.5")
    
    conv("ex3.1", "ex3.2")
    conv("ex3.1", "ex3.3")
    conv("ex3.1", "ex3.4")
    conv("ex3.1", "ex3.5")
    conv("ex3.2", "ex3.3")
    conv("ex3.2", "ex3.4")
    conv("ex3.2", "ex3.5")
    conv("ex3.3", "ex3.4")
    conv("ex3.3", "ex3.5")
    conv("ex3.4", "ex3.5")
    
    conv("ex4.1", "ex4.2")
    conv("ex4.1", "ex4.3")
    conv("ex4.1", "ex4.4")
    conv("ex4.1", "ex4.5")
    conv("ex4.2", "ex4.3")
    conv("ex4.2", "ex4.4")
    conv("ex4.2", "ex4.5")
    conv("ex4.3", "ex4.4")
    conv("ex4.3", "ex4.5")
    conv("ex4.4", "ex4.5")
    
    conv("ex5.1", "ex5.2")
    conv("ex5.1", "ex5.3")
    conv("ex5.1", "ex5.4")
    conv("ex5.1", "ex5.5")
    conv("ex5.2", "ex5.3")
    conv("ex5.2", "ex5.4")
    conv("ex5.2", "ex5.5")
    conv("ex5.3", "ex5.4")
    conv("ex5.3", "ex5.5")
    conv("ex5.4", "ex5.5")
    
    print("times")
    print(times)
    
csvfile = "outConv.csv"

#Assuming res is a flat list
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for t in times:
        writer.writerow([t])    