# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:46:48 2018

@author: kevin
"""

import subprocess as sp
import os
import itertools
import sys
import csv
import argparse as ap

#Runs strassenSeuil and returns the time it took to run the algorithm
def runProgram(m1, m2, threshold):
	print('Running ./strasseniSeuilCalcule -f', m1, m2, '-s', threshold) #KEVIN: run a commnand
	return float(sp.check_output(['./strassenSeuilCalcule', '-f', str(m1), str(m2), '-s', str(threshold)]))
	
def average(l):
	return sum(l) / len(l)

def runBenchmark(baseThreshold, matSizes):
	thresholds = [baseThreshold >> 2, baseThreshold, baseThreshold << 2, 1 << 30, 1]
	
	if not matSizes:
		matSizes = [7, 8, 9, 10, 11]
		
	matNumber = 5
	
	print('Generating matrices...')
	filenames = [['mat_' + str(size) + '_' + str(i) + '.txt' for i in range(0, matNumber)] for size in matSizes]
	matrixNumber = 1;
	for index, matGroup in enumerate(filenames):
		for filename in matGroup:
			print('Generating matrix', matrixNumber, '/', len(matSizes)*matNumber)
			matrixNumber = matrixNumber+1
			sp.call(['./Gen', str(matSizes[index]), filename])
	print('Matrix generation done.')
	
	print('Running benchmark...')
	
	with open('results.csv', 'wb') as csvFile:
		writer = csv.writer(csvFile, delimiter=',')
		writer.writerow(['Seuil', 'Matrix size'])
		writer.writerow([' '] + matSizes)
		for threshold in thresholds:
			row = [average([runProgram(combination[0], combination[1], threshold) for combination in itertools.combinations(matGroup, 2)]) for matGroup in filenames]
			writer.writerow([threshold] + row)
			print('Threshold =', threshold, ':', row)
			
	print('Benchmark done.')
			
	print("Removing generated matrices...")
	os.system("rm mat_*")
	
def findThreshold():
    #KEVIN: init vars
	matSize = 11
	bestThreshold = 0
	bestTime = sys.float_info.max #KEVIN: init to highest float value
	
	#Generate a test matrix
	sp.call(['./Gen', str(matSize), 'mat.txt'])
	
	print('Determining best threshold...')
	sys.stdout.flush()
	
	for i in [(1 << n) for n in range(2, matSize+1)]:
		time = runProgram('mat.txt', 'mat.txt', i);
		print('Threshold =', i, ':', time, 'seconds')
		sys.stdout.flush()
		
		if time < bestTime:
			bestTime = time
			bestThreshold = i
			
	print('########## Best threshold : ', bestThreshold, '##########')
	
	#Removing the test matrix
	sp.call(['rm', 'mat.txt'])
	
	return bestThreshold
	

parser = ap.ArgumentParser(description='Trouver le seuil approprie pour l\'algorithme de Strassen ou lancer un benchmark des performances.')
parser.add_argument('--threshold', type=int, help='Logarithme en base 2 du seuil de base a utiliser pour le benchmark', default=128)
parser.add_argument('--findThreshold', action='store_true', help='Trouve le meilleur seuil')
parser.add_argument('--benchmark', action='store_true', help='Lance un benchmark')
parser.add_argument('--mSizes', nargs='*', type=int, help='Logarithmes en base 2 des tailles des matrices a tester dans le benchmark')

args = parser.parse_args()

if args.findThreshold:
	threshold = findThreshold()
else:
	threshold = 2**args.threshold
	
if args.benchmark:
	runBenchmark(threshold, args.mSizes);
    
    