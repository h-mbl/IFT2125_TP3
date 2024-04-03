// Qiwu Wen, 20230961
// herve ngisse,20204609

#include "ClimbingDifficultyCalculator.h"
#include <fstream>
#include <vector>
// #include <unordered_set>
#include <math.h>
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

vector<int> splitStringToInts(const string& input) {
    istringstream stream(input);
    vector<int> result;
    string temp;
    
    while (getline(stream, temp, ',')) {
        result.push_back(stoi(temp));
    }

    return result;
}

int rightLeft(const std::vector<std::vector<int>>& dp, int i, int j,vector<vector<int>> wall) {
    int current = dp[i][j];
    int n = dp[0].size();
    int minVal = current; 

    if (j + 1 < n) {
        minVal = min(minVal, dp[i][j + 1] + wall[i][j]);
    }

    if (j - 1 >= 0) {
        minVal = min(minVal, dp[i][j - 1] + wall[i][j]);
    }

    return minVal;
}

int ClimbingDifficultyCalculator::CalculateClimbingDifficulty(std::string filename)
{
    ifstream monFichier("./wall1.txt");
    vector<vector<int>> wall;
    string ligne;

    if(monFichier.is_open())
    {
        
        while(getline(monFichier, ligne))
        {
            vector<int> colonne = splitStringToInts(ligne);
            wall.push_back(colonne);
            cout << ligne << endl;
        }
        monFichier.close();
    }
    else {
        cout << "impossible d'ouvrir le ficher" << endl;
        return -1; // Return -1 pour erreur
    }

    int m = wall.size();
    int n = wall[0].size();
    
    vector<vector<int>> dp(m, vector<int>(n));

    // Initialize the base row
    for (int j = 0; j < n; ++j) {
        dp[m-1][j] = wall[m-1][j];
    }

    
    
    int MAX = pow(2,25);
    
    
    //cout << ss << endl;

    // Fill the dp table
    for (int i = m - 2; i >= 0; --i) {

        for (int j = 0; j < n; ++j) {
            dp[i][j] = wall[i][j] + dp[i + 1][j]; 
        }

        bool updated = true;
    for (int k = 0; k < n - 1; ++k) {
        for (int j = 0; j < n; ++j) {
            
            dp[i][j] = rightLeft(dp, i, j, wall);
        }
    }
    }

    
   // cout << "DP Table:" << endl;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            cout << to_string(dp[i][j]) << " ";
    }
    cout << endl; // Move to the next line after printing each row
    }

    // Find the minimum difficulty path from the top row

    
    cout << "resultat est "<<*min_element(dp[0].begin(), dp[0].end()) << endl;
    return *min_element(dp[0].begin(), dp[0].end());
}

