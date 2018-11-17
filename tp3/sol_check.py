

################################################################################
#
# Ce script vérifie si votre solution est valide. C'est le script qui sera
# utilisé pour la correction, donc assurez-vous que la sortie de votre
# script tp.sh est compatible avec ce script-ci.
#
# Argument 1 : Path vers l'exemplaire
# Argument 2 : Path vers la solution de cet exemplaire
#
# Exemple d'utilisation :
#
#   1. Vous exécutez votre algorithme avec tp.sh et vous envoyez son résultat
#      vers un fichier texte :
#
#      ./tp.sh -e /home/pholi/INF4705/TP3/PCT_100_50 -p > sol_100_50.txt
#
#   2. Vous vérifiez si votre solution est valide avec ce script-ci :
#
#      python3 sol_check.py /home/pholi/INF4705/TP3/PCT_100_50 sol_100_50.txt
#
#
# Contactez-moi en cas de problème (philippe.olivier@polymtl.ca).
#
################################################################################


import pathlib
import sys


# Initial sanity checks
if (len(sys.argv) != 3):
    exit("ERREUR : Ce script de vérification de solution prend deux " + \
         "arguments en entrée. Voir le code source pour un exemple.")
if (not pathlib.Path(sys.argv[1]).is_file()):
    exit("ERREUR : Fichier " + sys.argv[1] + " inexistant.")
if (not pathlib.Path(sys.argv[2]).is_file()):
    exit("ERREUR : Fichier " + sys.argv[2] + " inexistant.")

# Parse instance
try:
    raw_instance = open(sys.argv[1]).readlines()
    raw_instance = [raw_instance[i][:-1] for i in range(len(raw_instance))]
    n = int(raw_instance[0])
    matrix = []
    for i in range(1, n+1):
        matrix.append([int(j) for j in raw_instance[i].split(' ')[:-1]])
    threshold = int(raw_instance[n+1])
    profits = [int(i) for i in raw_instance[n+2].split(' ')[:-1]]
except:
    exit("ERREUR : Problème avec le format de l'instance.")

# Parse solution
try:
    raw_solution = open(sys.argv[2]).readlines()
    raw_solution = raw_solution[-1]
    tour = raw_solution.split(' ')
    if ('\n' in tour[-1]):
        tour[-1] = tour[-1].strip('\n')
    if (tour[-1] == ''):
        tour = tour[:-1]
    tour = [int(i) for i in tour]
except:
    exit("ERREUR : Problème avec le format de la solution.")

# Ensure that all vertices are valid
for i in tour:
    if (i >= n):
        print("ERREUR : Le centre d'intérêt ", i, " n'existe pas (les centres d'intérêt sont numérotés de 0 à ", n-1, " pour cette instance).", sep='')
        exit(0)

# Ensure that the path is simple and closed
if (tour.count(0) != 2) or (tour[0] != 0) or (tour[-1] != 0):
    print("ERREUR : Le centre d'intérêt 0 (l'hôtel) doit être le premier ET le dernier centre visité, et ne peut pas être visité au milieu du parcours.")
    exit(0)
for i in range(1, n):
    if (tour.count(i) > 1):
        print("ERREUR : Le centre d'intérêt", i, "est visité plus d'une fois.")
        exit(0)

# Ensure that the cumulative cost is no greater than the threshold, and compute the profit
cumulative_costs = 0
cumulative_profits = 0
for i in range(len(tour)-1):
    cumulative_costs += matrix[tour[i]][tour[i+1]]
    cumulative_profits += profits[tour[i+1]]
if (cumulative_costs > threshold):
    print("ERREUR : La durée de votre parcours est de ", cumulative_costs, " alors que la durée limite pour l'instance est de ", threshold, ".", sep='')
    exit(0)

# Print the solution
print("Votre parcours est valide et sa qualité est de ", cumulative_profits, ".", sep='')
