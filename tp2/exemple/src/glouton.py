import sys

ex_path = sys.argv[1] # Path de l'exemplaire

# TODO: Algo ici

poids = []
poidsMax = 0

text_file = open(ex_path, "r")
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = lines[-1]

print(poids)
print(poidsMax)


options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé

