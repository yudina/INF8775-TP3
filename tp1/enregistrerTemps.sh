#!/bin/bash

# Ce script automatise l'exécution d'une batterie de tests
# Notez la structure des fichiers et répertoires pour cet exemple

for algo in {"conv","strassen","strassenSeuil"}; do
    for serie in $(ls "testset"); do
	counter=4
	for ex1 in $(ls "testset/$serie"); do
	    for ex2 in $(ls "testset/$serie" | tail -n $counter); do
		t=$(./tp.sh -a $algo -e testset/$serie/$ex1 testset/$serie/$ex2 -t)
		echo $t >> ./results/raw/${algo}_${serie}.csv
	    done
	    ((counter--))
	done
    done
done
