import sys
import time

ex_path = sys.argv[1]

text_file = open(ex_path, 'r')
next(text_file)
lines = text_file.read().split()
text_file.close()

poids = lines[1::2]
poidsMax = int(lines[-1])

for p in range(len(poids)):
    poids[p] = int(poids[p])

print("expected: ", poidsMax)
    
def calculPoids(poids, poidsMax):
    start = time.process_time()
    poidsPossible = []
    for i in range(poidsMax+1):
        if i>0:
            maximum = poidsPossible[i-1]
            for j in range(i):
                for k in poids:
                    if poidsPossible[j][0]+k>maximum[0] and poidsPossible[j][0]+k<=i:
                        p = []
                        for l in poidsPossible[j][1]:
                            p .append(l)
                        p.append(k)
                        maximum = (poidsPossible[j][0]+k, p)
                    if maximum[0]==i:
                        break
                if maximum[0]==i:
                    break
            poidsPossible.append(maximum)
        else:
            poidsPossible.append((0, []))
    end = time.process_time()
    return poidsPossible[-1], end-start

result, time = calculPoids(poids, poidsMax)
options = sys.argv[2:]
if '-p' in options: # On imprime la solution
  print(result) 
if '-t' in options: # On imprime le temps d'exécution
  print(time)