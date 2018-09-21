#!/bin/bash

# Ce script génère une série d'exemplaires
# Argument 1 : N de départ
# Argument 2 : nombre de N
# Argument 3 : germe

Nstart=$1
Nend=$((Nstart+$2-1))
germe=$3

for((N=$Nstart;N<=$Nend;N++)); do
    for I in {1..5}; do
	python3 generer_exemplaire.py $N "ex_"$N"."$I $((germe+$I))
    done
done
