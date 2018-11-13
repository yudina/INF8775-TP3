import sys

ex_path = "PR_100_400_1.txt"#sys.argv[1] # Path de l'exemplaire

#Lecture du fichier
text_file = open(ex_path, 'r')
next(text_file)
lines = text_file.read().split()
text_file.close()

#
poids = lines[1::2]
poidsMax = int(lines[-1])

for p in range(len(poids)):
  poids[p] = int(poids[p])

# La fonction retourne le poids total d’une solution
def somme():
    sum = 0
    for i in range (nbDyn):
    if sum + int(poids[i]) < int(poidsMax):
        sum += int(poids[i])

def voisin(v):
    S = 9;
#    Une solution voisine est obtenue en choisissant uniformément
#    au hasard un bâton parmi ceux qui ne sont pas encore choisis
#    et en l’ajoutant à la solution
    
#    Il est possible que cela rende le poids total supérieur à P :
#    on retirera alors des bâtons un à un (choisis uniformément au
#    hasard) jusqu’à ce que le poids total ne dépasse pas P
    
    return #solution voisine de la solution en paramètre


#def recuit(S0, T, kmax, P, α):
    S = S0;
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


options = sys.argv[2:]
if '-p' in options: # On imprime la solution
    print("84 73 12 44 98 75") # Données bidon, mais output du bon format demandé
if '-t' in options: # On imprime le temps d'exécution
    print("4.1347628746") # Données bidon, mais output du bon format demandé
