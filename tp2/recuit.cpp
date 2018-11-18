#include "recuit.hpp"
#include <stdlib.h>
#include <cmath>
#include <iostream>

#include <algorithm>

int Recuit::trouverSolution(int maxWeight, std::vector<Baton>& batons, std::vector<Baton>& resultat) {
    // resultat c'est S0
    double theta = 100;// T
	int kmax = 5;
    int p = 5;
    double alpha = 0.8;

    std::vector<Baton> solutionOptimale = resultat;
    
    for(size_t i = 0; i < kmax; i++)
    {
        for(size_t j = 0; j < p; j++)
        {
            std::vector<Baton> solutionAlternative = resultat;
            std::vector<Baton> batonsAlternative = batons;
            Recuit::choisirVoisin(maxWeight, batonsAlternative, solutionAlternative);
            double delta = Recuit::somme(solutionAlternative) - Recuit::somme(resultat);
            if (delta >= 0 || exp(delta/theta) >= (rand() / double(RAND_MAX))) {
                batons = batonsAlternative;
                resultat = solutionAlternative;
                if (Recuit::somme(solutionAlternative) > Recuit::somme(solutionOptimale)) {
                    solutionOptimale = resultat;
                }
            }
        }
        theta = theta * alpha;
    }
    
	//interface de David
    for(int i = 0; i < solutionOptimale.size(); ++i)
    {
        std::cout << solutionOptimale[i].getId() << " : " << solutionOptimale[i].getWeight() << std::endl;
    }
}
void Recuit::choisirVoisin(int maxWeight, std::vector<Baton>& batons, std::vector<Baton>& resultat) {
        auto it = Recuit::choisirBatonAleatoire(batons);
        resultat.push_back(*it);
        batons.erase(it);

        while(somme(resultat) > maxWeight) {
            auto it = Recuit::choisirBatonAleatoire(resultat);
            resultat.erase(it);
            batons.push_back(*it);
        }
}
std::vector<Baton>::iterator Recuit::choisirBatonAleatoire(std::vector<Baton>& batonRestants) {
    auto begin = batonRestants.begin();
    auto end = batonRestants.end();

    const unsigned long n = std::distance(begin, end);
    const unsigned long divisor = RAND_MAX / n;

    unsigned long k;
    do { k = std::rand() / divisor; } while (k >= n);

    std::advance(begin, k);
    return begin;
}

int Recuit::somme(std::vector<Baton>& batons) {
    int weight = 0;
    for(const auto& it : batons) 
    {
        weight += it.getWeight();
    }
    return weight;
}