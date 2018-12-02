import numpy
import random
from random import randrange
import sys
import time
from math import ceil, log

ex_path = "./instances/PCT_20_50" #sys.argv[1]

n_sites = 0
adj_matrix = [] # row will be start point, while column will be endpoint
max_time = 0
popularity = []

def extractData(file_name):
    global n_sites
    global max_time
    global popularity
    global adj_matrix
    
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
i_hotel = 0
popularity_hotel = 0
travel = [] # index, popularity, time
travel.append((i_hotel, popularity_hotel, adj_matrix[0][0])) # go to hotel
# END OF THE MAIN
index = 0

n_random_sites = int( (n_sites*0.6)-1 )
i_random_sites = random.sample(range(1, n_sites), n_random_sites)

for i in range(1, 3):
    i_previous = travel[i-1][0]
    travel.append((i_random_sites[i], popularity[i_random_sites[i]], adj_matrix[i_previous][i_random_sites[i]]))

travel.append((i_hotel, popularity_hotel, adj_matrix[0][0])) # TODO: close travel, go to hotel
print(travel)
