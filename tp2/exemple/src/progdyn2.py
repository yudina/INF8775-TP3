import sys
import time

ex_path = sys.argv[1] # Path de l'exemplaire
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

def dictionairePoids(poids):
  d = {}
  for p in poids:
    if p in d:
      d[p] = d[p]+1
    else:
      d[p] = 1
  return d

def somme(dictionaire):
  somme = 0
  for p in dictionaire:
    somme = somme + p*dictionaire[p]
  return somme

def calculPoids(poids, poidsMax):
  start = time.process_time()
  d = dictionairePoids(poids)
  pM = []
  for i in range(poidsMax+1):
    if i==0:
      pM.append({})
    elif i in poids:
      pM.append({i: 1})
    else:
      maximum = pM[i-1]
      for p in d:
        for j in range(i-1, -1, -1):
          if somme(pM[j])+p>somme(maximum) and somme(pM[j])+p<=i:
            if p in pM[j]:
              if pM[j][p]+1<=d[p]:
                maximum = pM[j]
                maximum[p] = maximum[p]+1
            else:
              maximum = pM[j]
              maximum[p] = 1
          if somme(maximum) == i:
            break
        if somme(maximum) == i:
          break
      pM.append(maximum)
  end = time.process_time()
  return pM[-1], end - start

result, time = calculPoids(poids, poidsMax)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
  print(result) 
if '-t' in options: # On imprime le temps d'exécution
  print(time) 