import sys
import time
from random import randrange

ex_path = "PR_100_400_1.txt"#sys.argv[1] # Path de l'exemplaire

poids = []
poidsMax = 0
nBatons = 0
start = 0
end = 0

def etraireListeBaton():
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
    global start
    global end
    start = time.process_time()
    sommeBatons = 0
    solution = []
    for i in range (nBatons):
        if sommeBatons + int(poids[i]) < int(poidsMax):
            sommeBatons += int(poids[i])
            solution.append(int(poids[i]))
    end = time.process_time()
    return solution
 
# La fonction retourne le poids total d’une liste de baton
def somme(batons):
    sommePoids = 0
    
    for i in range (batons):
        sommePoids += batons[i]
        
    return sommePoids

def choisirAleatoireBaton(batonsRestants):
    indexAleatoire = randrange(len(batonsRestants))
    print(batonsRestants[indexAleatoire])
    return indexAleatoire;
}

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
    while poidsMax < somme(resultat):
        resultatRetire = choisirAleatoireBaton(resultat)
        batons.append(resultat[nouveauBaton])
        del resultat[resultatRetire]

#    HOW YOU DO THIS ? : c'est déjà fait par globales i gauss
#    return #solution voisine de la solution en paramètre

def recuit(S0, T, kmax, P, α):
    S = glouton(solution)
#1 : La solution courante S est égale à une certaine solution initiale 
#       valide S0 (par exemple la solution de votre algorithme glouton).
#2 : On garde en mémoire la meilleure solution trouvée jusqu’à présent.
#3 : La température courante θk  est égale à la température initiale T.
#4 et 5: Pour chacune des kmax itérations et pour chacun des P paliers de température.
#6 : On génère une nouvelle solution S’ (voisine de la solution S).
#7 à 9 : Si la nouvelle solution est meilleure que la solution courante ou si la
#       condition de probabilité est rencontrée, on met à jour la solution courante.
#10 et 11 : On met à jour la meilleure solution si nécessaire.
#15 : On met à jour la température.
#16 : En terminannt l’algorithme retourne la meilleure solution qu’il a pu trouver.

#1	S ← S0
#2	Smeilleur ← S
#3	θ1 ← T
#4	for k = 1 ... kmax do
#5		for j = 1 ... P do
#6			S’ ← voisin(S)
#7			Δ ← somme(S’) - somme(S)
#8			if Δ ≥ 0 or eΔ/θk ≥ unif([0,1]) then
#9				S ← S’
#10				if somme(S) > somme(Smeilleur) then
#11					Smeilleur ← S
#12				end if
#13			end if
#14		end for
#15		θk+1 ← θk × α
#16	end for
#17	retourner Smeilleur

def imprimerSolution(s):
    sortie = ""
    for i in range(len(s)):
        sortie += str(s[i]) + " "
    print(sortie)

options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
