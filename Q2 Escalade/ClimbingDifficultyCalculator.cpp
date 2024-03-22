// Nom, Matricule
// Nom, Matricule

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
// #include <unordered_set>
// #include <math.h>
#include <iostream>
#include <algorithm>

using namespace std;

// ce fichier contient les definitions des methodes de la classe ClimbingDifficultyCalculator
// this file contains the definitions of the methods of the ClimbingDifficultyCalculator class

ClimbingDifficultyCalculator::ClimbingDifficultyCalculator()
{
}

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    // TODO
    // Création d'un vecteur (tableau dynamique) de taille donnée
    std::vector<std::vector<int>> matrice ;
    std::ifstream fichier(filename);
    if (fichier.is_open()) {
        std::cerr << "Erreur lors de l'ouverture du fichier." << std::endl;
        return -1; // Retourne une valeur d'erreur
    }

    std::string ligne;
    while (std::getline(fichier, ligne)) { // Lire chaque ligne du fichier
        std::vector<int> ligne_entiers; // Vecteur pour stocker les entiers de chaque ligne

        // Conversion de la chaîne en vecteur d'entiers
        std::string nombre;
        for (char c : ligne) {
            if (c == ',') { // Si c'est une virgule, convertir le nombre et l'ajouter au vecteur
                int entier = std::stoi(nombre);
                ligne_entiers.push_back(entier);
                nombre.clear(); // Réinitialiser la chaîne pour le prochain nombre
            } else {
                nombre += c; // Ajouter le caractère au nombre
            }
        }
        // Ajouter le dernier nombre de la ligne
        int entier = std::stoi(nombre);
        ligne_entiers.push_back(entier);

        matrice.push_back(ligne_entiers); // Ajouter le vecteur de la ligne à la matrice
    }

    // Affichage de la matrice (pour le test)
    std::cout << "Matrice : " << std::endl;
    for (const auto& ligne : matrice) {
        for (int entier: ligne) {
            std::cout << entier << " ";
        }
        std::cout << std::endl;
    }

    fichier.close(); // Fermer le fichier une fois la lecture terminée

    // ---- En supposant que la matrice a ete bien initialise.
    //j'inverse la matrice car le dernier element sera le premier
    // Inversion du vecteur
    std::reverse(matrice.begin(), matrice.end());
    

    return 0;
}
