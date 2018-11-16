import os             
all_files = os.listdir("../../jeux_de_donnees/dyn1r")  
print(all_files) 

import os

for i in zip(all_files):
    os.system('py progdyn1.py ../../jeux_de_donnees/dyn1r/%s -r' % (i))