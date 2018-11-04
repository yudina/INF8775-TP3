import sys
import time

ex_path = sys.argv[1] # Path de l'exemplaire

# TODO: Algo ici
start = time.process_time()
poids = []
poidsMax = 0

text_file = open(ex_path, "r")
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = lines[-1]
poids = sorted(poids, key=int, reverse=True) 
#print(poids)
#print(poidsMax)

nbDyn = len(poids)

sum = 0
for i in range (nbDyn):
    if sum + int(poids[i]) < int(poidsMax):
        sum += int(poids[i])
end = time.process_time()

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print(sum)
if '-t' in options: # On imprime le temps d'exécution
    print(end - start, "seconds")