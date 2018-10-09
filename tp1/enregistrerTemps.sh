# note : le script est mal concu, il faudra l'arreter manuellement avec ctrl+c

ex_folder="testset"
for algo in "insertion"; do # parametres possibles : insertion, merge, mergeSeuil
    for testset_folder in $(ls $ex_folder); do
        for ex in $(ls ${ex_folder}); do
			echo ${algo} ${ex}
            # On évalue la taille de l'exemplaire.
            size=$(echo $ex | cut -d_ -f2)
	    	# On note le temps d'exécution dans t.
			t=$(./tp.sh -a $algo -e ${ex_folder}/${ex} -t) # ajouter un timeout si ca dure une eternite...
	    	# Si le temps n'est pas nul, on le note dans le csv.
            if [ t != "" ]; then
				echo $size,$t >> results/raw/${algo}.csv
            fi
        done
    done
done