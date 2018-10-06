# Ce script génère un exemplaire (une matrice)
# Argument 1 : N
# Argument 2 : nom du fichier de sortie
# Argument 3 : germe

import random
import sys

N = int(sys.argv[1])
nom = sys.argv[2]
germe = int(sys.argv[3])

random.seed(germe)

with open(nom, 'w') as f:
    f.write(str(N)+'\n')
    for i in range(2**N):
        for j in range(2**N):
            f.write(str(random.randint(0, 10))+'\t')
        f.write('\n')
        
f.close()
