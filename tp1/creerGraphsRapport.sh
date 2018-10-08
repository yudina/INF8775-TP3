#!/bin/bash

for data in $(ls results/tests/rapport_opt/)
do
	sed -i 's/,/ /g' results/tests/rapport_opt/$data
	gnuplot -e "set xlabel \"Taille\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_rapport_opt.png\"; 
	plot \"results/tests/rapport_opt/$data\" with linespoints"
done

for data in $(ls results/tests/rapport_worst/)
do
	sed -i 's/,/ /g' results/tests/rapport_worst/$data
	gnuplot -e "set xlabel \"Taille\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_rapport_worst.png\"; 
	plot \"results/tests/rapport_worst/$data\" with linespoints"
done
