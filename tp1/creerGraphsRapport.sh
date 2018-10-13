#!/bin/bash

for data in $(ls results/tests/rapport/)
do
	sed -i 's/,/ /g' results/tests/rapport/$data
	gnuplot -e "set xlabel \"Taille de l'exemplaire 2^N\" offset 2.1; 
	set ylabel \"Rapport du temps sur hypothese f(x)\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_rapport.png\"; 
	plot \"results/tests/rapport/$data\" with linespoints"
done
