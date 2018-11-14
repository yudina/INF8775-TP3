import sys
import time

ex_path = "PR_100_400_1.txt" #sys.argv[1] # Path de l'exemplaire

# TODO: Algo ici

poids = []
poidsMax = 0

text_file = open(ex_path, "r")
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = lines[-1]
poids = sorted(poids, key=int, reverse=True) # Trie les bâtons en ordre décroissant

nbDyn = len(poids)

start = time.process_time()
sommeBatons = 0
solution = []
for i in range (nbDyn):
    if sommeBatons + int(poids[i]) < int(poidsMax):
        sommeBatons += int(poids[i])
        solution.append(int(poids[i]))
end = time.process_time()

def imprimerSolution(s):
    sortie = ""
    for i in range(len(s)):
        sortie += str(s[i]) + " "
    print(sortie)

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    imprimerSolution(solution)
if '-t' in options: # On imprime le temps d'exécution
    print(end - start)
