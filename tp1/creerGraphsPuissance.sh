#!/bin/bash

for data in $(ls results/mean/)
do
	sed -i 's/,/ /g' results/mean/$data
	gnuplot -e "set xlabel \"Taille\" offset 2.1; 
	set ylabel \"Temps\" offset 2.1;
	set logscale xy; 
	set term png;
	set term png size 800, 650; 
	set size 1,1;
	set output \"graphs/${data%.csv}_puissance.png\"; 
	f(x)=a*x**b; 
	fit f(x) \"results/mean/$data\" via a, b; 
	plot \"results/mean/$data\" with points, f(x) with lines title sprintf('Courbe de puissance f(x) = %.8f·x^{%.8f}', a, b)"
done
