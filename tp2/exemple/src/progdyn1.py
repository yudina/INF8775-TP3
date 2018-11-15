import sys
import time

ex_path = "WC-10-10-01.txt" #sys.argv[1] # Path de l'exemplaire

text_file = open(ex_path, 'r')
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = int(lines[-1])

for p in range(len(poids)):
  poids[p] = int(poids[p])

#print("expected: ", poidsMax)

def calculPoids(poids, poidsMax):
	start = time.process_time()
	poidsPossible = []
	for i in range(poidsMax+1):
	    maximum = 0
	    if i>0:
	        maximum = poidsPossible[i-1]
	    for j in range(i):
	        for k in poids:
	            if poidsPossible[j]+k>maximum and poidsPossible[j]+k<=i:
	                maximum = poidsPossible[j]+k
	            elif poidsPossible[j]+k==i:
	                maximum = i
	                break
	        if maximum == i:
	            break
	    poidsPossible.append(maximum)
	end = time.process_time()
	return poidsPossible[-1], end - start

result, time = calculPoids(poids, poidsMax)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
  print("calcul: ", result) 
if '-t' in options: # On imprime le temps d'exécution
  print(time, "seconds") 
