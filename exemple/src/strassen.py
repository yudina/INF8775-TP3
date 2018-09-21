import sys

ex_path1 = sys.argv[1] # Path de la première matrice
ex_path2 = sys.argv[2] # Path de la deuxième matrice

# TODO: Algo de multiplication de matrices ici (dans le cas de strassen.py, l'algo de Strassen)

options = sys.argv[3:]
if '-p' in options: # On imprime la matrice résultat
    print("2\n1\t2\t3\t4\n5\t6\t7\t8\n9\t10\t11\t12\n13\t14\t15\t16") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
