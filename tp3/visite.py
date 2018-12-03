import numpy
import random
from random import randrange
import sys
import time
from math import ceil, log

ex_path = "./instances/PCT_20_50" #sys.argv[1]

cumul_time = 0
relative_e = 0.20
total_popularity = 0
n_sites = 0
adj_matrix = [] # row will be start point, while column will be endpoint
density_adj = []
avail_popularity = []
max_time = 0
popularity = []
travel = [] # index, popularity, time

I_HOTEL = 0
POP_HOTEL = 0

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


# greedy with density
def calculateDensityAdj():
    global density_adj
    density_adj = [[0.0 for x in range(n_sites)] for y in range(n_sites)]
    
    for i in range(n_sites):
        for j in range (n_sites):
            if (i != j & popularity[j] != 0.0):
                density_adj[i][j] = adj_matrix[i][j] / popularity[j]
            else:
                density_adj[i][j] = adj_matrix[i][j]

def randomBeginTravel():
    global travel
    global cumul_time
    global avail_popularity
    
    # generate n_sites*0.6 random indexes for the beginning of the travel
    n_random_sites = int( (n_sites*0.6) )
    i_random_sites = random.sample(range(1, n_sites), n_random_sites)
    
    cumul_time = 0
    
    # choose random sites
    for i in range(1, n_random_sites):
        if (cumul_time <= max_time):
            i_previous_site = travel[i-1][0]
            new_time = adj_matrix[i_previous_site][i_random_sites[i]]
            
            # add the next random site.
            # index, popularity, time (row = previous site, column = current site)
            travel.append((i_random_sites[i], popularity[i_random_sites[i]], adj_matrix[i_previous_site][i_random_sites[i]]))
            cumul_time += new_time
            if (cumul_time >= max_time):
                cumul_time -= new_time
                break
        else:
            break
    
    # remove visited, and place non-visited in a copy
    visited = sorted(i_random_sites, key=int, reverse=True)
    avail_popularity = popularity.copy()
    
    for i in range(len(visited)):
        j = visited[i]
        avail_popularity.remove(avail_popularity[j])
    
    
# THE MAIN
extractData(ex_path);
start_time = time.time()
calculateDensityAdj();
travel.append((I_HOTEL, POP_HOTEL, adj_matrix[0][0])) # go to hotel
randomBeginTravel();


# END OF THE MAIN

print(density_adj)

# TODO: close travel. Temporary : go to hotel (wrong time from previous to hotel)
travel.append((I_HOTEL, POP_HOTEL, adj_matrix[0][0]))
#print(travel)
