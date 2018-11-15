import sys
import time

ex_path = sys.argv[1] # Path de l'exemplaire
n = int(sys.argv[2])
# TODO: Algo ici

text_file = open(ex_path, 'r')
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = int(lines[-1])

for p in range(len(poids)):
  poids[p] = int(poids[p])

print("expected: ", poidsMax)

def matricePoids(n, poidsMax):
	m = [[0 for _ in range(poidsMax)] for _ in range(n)]
	return m

def calculPoids(nbBatons, poids, poidsMax):
  #n = calculBatons(poids, poidsMax)
  start = time.process_time()
  m = matricePoids(nbBatons, poidsMax)
  for i in range(nbBatons):
    for j in range(poidsMax):
      if i == 0:
        if j+1 in poids:
          m[i][j] = j+1
        elif j != 0:
          m[i][j] = m[i][j-1]
        else:
          m[i][j] = 0
      else:
        maximum = 0
        for k in range(j):
          for p in poids:
            if m[i-1][k]+p <= j+1 and m[i-1][k]+p > maximum:
              maximum = m[i-1][k]+p
        m[i][j] = maximum
  end = time.process_time()
  return m[-1][-1], end - start

result, time = calculPoids(n, poids, poidsMax)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
  print("calcul: ", result) 
if '-t' in options: # On imprime le temps d'exécution
  print(time, "seconds") 
