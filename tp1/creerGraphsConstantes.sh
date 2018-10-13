#!/bin/bash

for data in $(ls results/tests/constantes/)
do
	sed -i 's/,/ /g' results/tests/constantes/$data
	gnuplot -e "set xlabel \"Hypothese f(x)\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_constantes.png\"; 
	f(x)=a*x; fit f(x) \"results/tests/constantes/$data\" via a; 
	plot \"results/tests/constantes/$data\" with points, f(x) with lines title sprintf('f(x) = %e·x+{%.8f}', a, b)"
done
