# Vérifions que nos algorithmes fonctionnent correctement
ex_folder="testset"
for algo in {"insertion","merge","mergeSeuil"}; do
	for testset_folder in $(ls $ex_folder); do
		for ex in $(ls ${ex_folder}); do
			# sort -n -c permet de regarder si notre output est trié
			./tp.sh -a $algo -e ./${ex_folder}/${ex} -p | sort -n -c
		done
	done
done
