#!/bin/bash

for data in $(ls results/tests/constantes_opt/)
do
	sed -i 's/,/ /g' results/tests/constantes_opt/$data
	gnuplot -e "set xlabel \"Taille\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_constantes_opt.png\"; 
	f(x)=a*x; fit f(x) \"results/tests/constantes_opt/$data\" via a; 
	plot \"results/tests/constantes_opt/$data\" with points, f(x) with lines title sprintf('f(x) = %e·x+{%.8f}', a, b)"
done

for data in $(ls results/tests/constantes_worst/)
do
	sed -i 's/,/ /g' results/tests/constantes_worst/$data
	gnuplot -e "set xlabel \"Taille\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set autoscale xy; 
	set term png;
	set term png size 800, 650; 
	set output \"graphs/${data%.csv}_constantes_worst.png\"; 
	f(x)=a*x; fit f(x) \"results/tests/constantes_worst/$data\" via a; plot \"results/tests/constantes_worst/$data\" with points, f(x) with lines title sprintf('f(x) = %e·x+{%.8f}', a, b)"
done
