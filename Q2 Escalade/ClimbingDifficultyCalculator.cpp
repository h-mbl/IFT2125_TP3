// Nom, Matricule
// Nom, Matricule

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
// #include <unordered_set>
// #include <math.h>
#include <iostream>
#include <algorithm>

//add
#include <sstream>

using namespace std;

// ce fichier contient les definitions des methodes de la classe ClimbingDifficultyCalculator
// this file contains the definitions of the methods of the ClimbingDifficultyCalculator class

ClimbingDifficultyCalculator::ClimbingDifficultyCalculator()
{
}

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    ifstream monFichier("./wall1.txt");

    if(monFichier.is_open())
    {
        string ligne;
        while(getline(monFichier, ligne))
        {
            cout << ligne << endl;
        }
    }
    else
    {
        cout << "Impossible d'ouvrir le fichier" << endl;
    }
}

