import sys
import time
import math
import random
from random import randrange

ex_path = sys.argv[1] # Path de l'exemplaire

# variables globales (pour remplacer les passages par référence)
poids = []
poidsMax = 0
nbDyn = 0

# Recuit et voisin
poidsPrime = 0
SPrime = 0

# temps
debut = 0
fin = 0
temps = 0

def extraireListeBatons():
    text_file = open(ex_path, "r")
    next(text_file)
    lines = text_file.read().split()
    text_file.close()
    
    global poids
    global poidsMax
    global nbDyn
    poids = lines[1::2]
    poidsMax = int(lines[-1])
    poids = sorted(poids, key=int, reverse=True) # Trie les bâtons en ordre décroissant
    poids = [ int(x) for x in poids ]
    nbDyn = len(poids)

def glouton():
    sommeBatons = 0
    solution = []
    for i in range (nbDyn):
        if sommeBatons + poids[i] < poidsMax:
            sommeBatons += poids[i]
            solution.append(poids[i])
    return solution
 
# La fonction retourne le poids total d’une liste de baton
def somme(batons):
    sommePoids = 0
    
    for i in range (len(batons)):
        sommePoids += int(batons[i])
        
    return sommePoids

# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
def choisirAleatoireBaton(batons):
    indexAleatoire = randrange(len(batons))
    return indexAleatoire;

#https://stackoverflow.com/questions/627435/how-do-i-remove-an-element-from-a-list-by-index-in-python
def voisin():
    global poidsPrime
    global SPrime
    #    Une solution voisine est obtenue en choisissant uniformément
    #    au hasard un bâton parmi ceux qui ne sont pas encore choisis
    #    et en l’ajoutant à la solution
    nouveauBaton = choisirAleatoireBaton(poidsPrime)
    SPrime.append(poidsPrime[nouveauBaton])
    del poidsPrime[nouveauBaton]
    
    #    Il est possible que cela rende le poids total supérieur à P :
    #    on retirera alors des bâtons un à un (choisis uniformément au
    #    hasard) jusqu’à ce que le poids total ne dépasse pas P
    while int(poidsMax) < somme(SPrime):
        resultatRetire = choisirAleatoireBaton(SPrime)
        poidsPrime.append(SPrime[resultatRetire])
        del SPrime[resultatRetire]

def recuit(poids, S0):#(S0, T, kmax, P, α):
    global poidsPrime
    global SPrime
    
    theta = 100 # T
    kmax = 5
    P = 5
    alpha = 0.8
    
    solutionRecuit = S0
    
    for i in range (kmax):
        for j in range (P):
            SPrime = S0
            poidsPrime = poids
            
            voisin()# les arguments par réf. sont théoriquement poidsPrime, SPrime
            
            delta = somme(SPrime) - somme(S0)
            exposant = math.exp(delta/theta)
            if (0 <= delta or random.uniform(0, 1) <= exposant ):
                poids = poidsPrime
                S0 = SPrime
                if (somme(solutionRecuit) <= somme(SPrime)):
                    solutionRecuit = S0
        theta = theta * alpha
        return solutionRecuit

def imprimerSolution(s):
    sortie = ""
    for i in range(len(s)):
        sortie += str(s[i]) + " "
    print(sortie)

# Le "main"
extraireListeBatons()

debut = time.process_time()
S0 = glouton()
solutionRecuit = recuit(poids, S0)
fin = time.process_time()
temps = fin - debut

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    imprimerSolution(solutionRecuit)
if '-t' in options: # On imprime le temps d'exécution
    print(temps)
