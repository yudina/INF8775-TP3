import os             
all_files = os.listdir("../../jeux_de_donnees")  
print(all_files) 

import os

for i in zip(all_files):
    os.system('python3 glouton2.py ../../jeux_de_donnees/%s -t' % (i))