import os             
all_files = os.listdir("../../jeux_de_donnees/dyn1l")  
print(all_files) 

import os

for i in zip(all_files):
    os.system('py progdyn1.py ../../jeux_de_donnees/dyn1l/%s -r' % (i))