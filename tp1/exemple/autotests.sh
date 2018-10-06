#!/bin/bash

# Ce script automatise l'exécution d'une batterie de tests
# Notez la structure des fichiers et répertoires pour cet exemple

for algo in {"conv","strassen","strassenSeuil"}; do
    for serie in $(ls "exemplaires"); do
	counter=4
	for ex1 in $(ls "exemplaires/$serie"); do
	    for ex2 in $(ls "exemplaires/$serie" | tail -n $counter); do
		t=$(./tp.sh -a $algo -e $serie/$ex1 $serie/$ex2 -t)
		echo $t >> ./resultats/${algo}_${serie}.csv
	    done
	    ((counter--))
	done
    done
done
