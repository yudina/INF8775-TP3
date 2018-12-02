import numpy
from random import randrange
import sys
import time
from math import ceil, log

ex_path = "./instances/PCT_20_50" #sys.argv[1]

n_sites = 0
max_time = 0
popularity = []

def extractData(file_name):
    global n_sites
    global max_time
    global popularity
    adj_matrix = []
    
    # obtain every line as int list
    with open(file_name,'r') as ex:
        for line in ex:
            line = line.strip()
            if len(line) > 1:
               adj_matrix.append([int(a) for a in line.split()])
           
    # collect data
    n_sites = adj_matrix[0][0]
    max_time = adj_matrix[-2][0]
    popularity = adj_matrix[-1]
    
    # delete first, second to last and last rows
    adj_matrix.remove(adj_matrix[0])
    adj_matrix.remove(adj_matrix[-2])
    adj_matrix.remove(adj_matrix[-1])
    
#    print(n_sites)
#    print(max_time)
#    print(popularity)
#    print(adj_matrix)


# THE MAIN
extractData(ex_path);

# END OF THE MAIN
index = 0

random_index = randrange(len(popularity))
print("index")
print(random_index)
print(popularity[random_index])
