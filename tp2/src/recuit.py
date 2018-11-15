import sys
import time
import math
import random
from random import randrange

ex_path = "PR_100_400_1.txt"#sys.argv[1] # Path de l'exemplaire

# variables globales (pour remplacer les passages par référence)
poids = []
poidsMax = 0
nBatons = 0
debut = 0
fin = 0
temps = 0

def extraireListeBaton():
    text_file = open(ex_path, "r")
    next(text_file)
    lines = text_file.read().split()
    text_file.close()
    
    global poids
    global poidsMax
    global nBatons
    poids = lines[1::2]
    poidsMax = lines[-1]
    poids = sorted(poids, key=int, reverse=True) # Trie les bâtons en ordre décroissant
    
    nBatons = len(poids)

def glouton():
    global nBatons
    sommeBatons = 0
    solution = []
    for i in range (nBatons):
        if sommeBatons + int(poids[i]) < int(poidsMax):
            sommeBatons += int(poids[i])
            solution.append(int(poids[i]))
    return solution
 
# La fonction retourne le poids total d’une liste de baton
def somme(batons):
    sommePoids = 0
    
    for i in range (len(batons)):
        sommePoids += int(batons[i])
        
    return sommePoids

# https://stackoverflow.com/questions/306400/how-to-randomly-select-an-item-from-a-list
def choisirAleatoireBaton(batonsRestants):
    indexAleatoire = randrange(len(batonsRestants))
    return indexAleatoire;

#https://stackoverflow.com/questions/627435/how-do-i-remove-an-element-from-a-list-by-index-in-python
def voisin(poidsMax, batons, resultat):
    #    Une solution voisine est obtenue en choisissant uniformément
    #    au hasard un bâton parmi ceux qui ne sont pas encore choisis
    #    et en l’ajoutant à la solution
    nouveauBaton = choisirAleatoireBaton(batons)
    resultat.append(batons[nouveauBaton])
    del batons[nouveauBaton]
    
    #    Il est possible que cela rende le poids total supérieur à P :
    #    on retirera alors des bâtons un à un (choisis uniformément au
    #    hasard) jusqu’à ce que le poids total ne dépasse pas P
    while int(poidsMax) < somme(resultat):
        resultatRetire = choisirAleatoireBaton(resultat)
        batons.append(resultat[resultatRetire])
        del resultat[resultatRetire]

#    HOW YOU DO THIS ? : c'est déjà fait par globales i gauss
#    return #solution voisine de la solution en paramètre

def recuit(poidsMax, batons, resultat):#(S0, T, kmax, P, α):
    
    # resultat c'est S0
    theta = 100 # T
    kmax = 5
    P = 5
    alpha = 0.8

    solutionOptimale = resultat
    
    for i in range (kmax):
        for j in range (P):
            solutionAlternative = resultat
            batonsAlternatives = batons
            voisin(poidsMax, batonsAlternatives, solutionAlternative)
            delta = somme(solutionAlternative) - somme(resultat)
            exposant = math.exp(delta/theta)
            if (0 <= delta or random.uniform(0, 1) <= exposant ):
                batons = batonsAlternatives
                resultat = solutionAlternative
                if (somme(solutionOptimale) <= somme(solutionAlternative)):
                    solutionOptimale = resultat
        theta = theta * alpha
        return solutionOptimale

def imprimerSolution(s):
    sortie = ""
    for i in range(len(s)):
        sortie += str(s[i]) + " "
    print(sortie)

extraireListeBaton()
debut = time.process_time()
resultat = glouton()
solutionOptimale = recuit(poidsMax, poids, resultat)
fin = time.process_time()
temps = fin - debut
imprimerSolution(solutionOptimale)
print(temps)

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    imprimerSolution(solutionOptimale) # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print(temps) # Données bidon, mais output du bon format demandé
