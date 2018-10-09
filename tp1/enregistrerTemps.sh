#!/bin/bash

# Ce script automatise l'exécution d'une batterie de tests
# Notez la structure des fichiers et répertoires pour cet exemple

for algo in {"conv","strassen","strassenSeuil"}; do
    for serie in $(ls "testset"); do
	echo "EXECUTION 1" >> ./results/raw/${algo}_${serie}.csv
	counter=4
	for ex1 in $(ls "testset/$serie"); do
	    for ex2 in $(ls "testset/$serie" | tail -n $counter); do
		t=$(./tp.sh -a $algo -e $serie/$ex1 $serie/$ex2 -t)
		echo $t >> ./results/raw/${algo}_${serie}.csv
	    done
	    ((counter--))
	done
    done
done

# # note : le script est mal concu, il faudra l'arreter manuellement avec ctrl+c
# ex_folder="testset"
# for algo in {"conv","strassen","strassenSeuil"}; do # parametres possibles : conv, strassen et strassenSeuil
    # for testset_folder in $(ls $ex_folder); do
	# counter=4
        # for ex in $(ls ${ex_folder}); do
			# echo ${algo} ${ex}
            # # On évalue la taille de l'exemplaire.
            # size=$(echo $ex | cut -d_ -f2)
	    	# # On note le temps d'exécution dans t.
			# t=$(./tp.sh -a $algo -e ${ex_folder}/${ex} ${ex_folder}/${ex} -t) # ajouter un timeout si ca dure une eternite...
	    	# # Si le temps n'est pas nul, on le note dans le csv.
            # if [ t != "" ]; then
				# echo $size,$t >> results/raw/${algo}.csv
            # fi
        # done
    # done
# done
