import sys
import time

ex_path = "PR_100_400_1.txt"#sys.argv[1] # Path de l'exemplaire

poids = []
poidsMax = 0

text_file = open(ex_path, "r")
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = int(lines[-1])
poids = sorted(poids, key=int, reverse=True) # Trie les bâtons en ordre décroissant

poids = [ int(x) for x in poids ]

nbDyn = len(poids)

start = time.process_time()
sommeBatons = 0
solution = []
for i in range (nbDyn):
    if sommeBatons + poids[i] < poidsMax:
        sommeBatons += poids[i]
        solution.append(poids[i])
        del poids[i]
    else:
        break
end = time.process_time()

def imprimerSolution(solution):
    sortie = ""
    for i in range(len(solution)):
        sortie += str(solution[i]) + " "
    print(sortie)

imprimerSolution(solution)

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    imprimerSolution(solution)
if '-t' in options: # On imprime le temps d'exécution
    print(end - start)
