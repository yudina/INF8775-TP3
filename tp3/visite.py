import random
from random import randrange
import sys
from math import ceil, log

ex_path = "./instances/PCT_200_50" #sys.argv[1]

# file data
n_sites = 0
adj_matrix = [] # row will be start point, while column will be endpoint
max_time = 0
popularity = []

# probabilistic
I_HOTEL = 0
POP_HOTEL = 0

# travel attributes
travel = [] # list, tuple index, popularity, time

# greedy
density_line = []
avail_popularity = []

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

# probabilist algorithm
def randomBeginTravel():
    global travel
    global avail_popularity
    
    # generate n_sites*0.35 random indexes for the beginning of the travel
    n_random_sites = int( (n_sites)*0.35 ) # *27/31)-5) )
    i_random_sites = random.sample(range(1, n_sites), n_random_sites)
    
    cumul_time = 0
    
    # choose random sites
    for i in range(1, n_random_sites):
        if (cumul_time <= max_time):
            i_previous_site = travel[i-1][0]
            new_time = adj_matrix[i_previous_site][i_random_sites[i]]
            
            # check if can add the next random site.
            # travel tuplet : site index, site popularity, travel time to site
            if (cumul_time + new_time <= max_time):
                travel.append((i_random_sites[i], popularity[i_random_sites[i]], new_time))
                cumul_time += new_time
            else: # max_time reached
                break
        else:
            break
    
    # copy popularity, and remove visited sites in the copy
    # visited is reversed, so we delete elements in decreasing order of index
    visited = sorted(i_random_sites, key=int, reverse=True)
    avail_popularity = []
    
    # avail_popularity contains the index of unvisited sites
    for i in range(n_sites):
        avail_popularity.append(i)
    
    # remove visited places
    for i in range(len(visited)):
        j = visited[i]
        avail_popularity.remove(avail_popularity[j])
        
    avail_popularity.remove(0) # remove hotel

# calculate total time of travel
def calculate_cumul(trav):
    total = 0
    for i in range(len(trav)):
        total += trav[i][2]
    return total

# calculate total popularity of travel
def calculate_pop(trav):
    total = 0
    for i in range(len(trav)):
        total += trav[i][1]
    return total

# return de density matrix for the row i_current_site (last site of the travel)
def calculateDensityLine(i_current_site):
    d_line = []
    for i in range(n_sites):
        if (adj_matrix[i_current_site][i] != 0):
            d_line.append( (popularity[i]/adj_matrix[i_current_site][i], i) )
        else:
            d_line.append( (0, i) )
    return d_line

# sort density in decreasing order, then return the index of the highest possible
# density (a density which column corresponds to a free n in avail_popularity)
def maxDensity(d_line, a_popularity):
    sorted_d_line = []
    
    sorted_d_line = sorted(d_line, key=lambda x: x[0], reverse=True)
    
    for i in range(len(sorted_d_line)):
        if(sorted_d_line[i][1] in a_popularity):
            return a_popularity[i]
    return 0

def findGreedyTravel():
    global travel
    global avail_popularity
    global density_line
    
    avail_len = len(avail_popularity)
    for i in range(avail_len):
        
        cumul_time = calculate_cumul(travel)
        
        if(cumul_time <= max_time):
            # current row index is index of current travel site
            i_current_site = travel[-1][0]
            density_line = calculateDensityLine(i_current_site)
            
            # get the index of the maximum available density
            i_max_density = maxDensity(density_line, avail_popularity)
            
            # time from current site to new site
            new_time = adj_matrix[i_current_site][i_max_density]
            
            # check if can add the new site
            # travel tuplet : site index, site popularity, travel time to site
            if (cumul_time + new_time <= max_time):
                travel.append((i_max_density, popularity[i_max_density], new_time))
                avail_popularity.remove(i_max_density)
            else: # max_time reached
                break
        else:
            break
        

# THE MAIN
extractData(ex_path)
travel.append((I_HOTEL, POP_HOTEL, adj_matrix[0][0])) # go to hotel
randomBeginTravel()
findGreedyTravel()
# END OF THE MAIN

        
print(travel)
print(cumul_time)
print(calculate_pop(travel))

# Determine if should continue
optimal = sum(popularity)
print(optimal)
#print(runtime);
