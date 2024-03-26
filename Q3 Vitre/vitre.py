#Nom, matricule
#Nom, matricule
import sys
#Fonction à compléter. Ne modifiez pas sa signature.
#N : Force maximale
#k : Nombre de fenêtres disponibles
#Valeur de retour : le nombre minimal de tests qu'il faut faire 
#                   en pire cas pour déterminer le seuil de solidité 
#                   d'une fenêtre
#Doit retourner la réponse comme un int.
#
#Function to complete. Do not change its signature.
#N : Maximum force
#k : Number of windows available
#return value : Minimum number of tests needed in the worst case
#               to find the solidity threshold of a window
#Must return the answer as an int. 
def calcul_value(start, end, k, table):
    if k == 1:
        return end - start   # cas de base
    if start >= end:
        return 0 #valeur invalide
    if table[start][end][k] != 0:  # memorisation
        return table[start][end][k]

    min_val = 999999999 # valeur minimale

    for i in range(start, end + 1):  #i est la position courante

        # nombre de lance maximal entre deux parties(vitre casse ou vitre non casse) dans le pire cas
        cost = 1 + max(calcul_value(start, i-1, k, table), calcul_value(i, end, k-1, table))
        # cout minimale
        min_val = min(min_val, cost)

    table[start][end][k] = min_val  # Memoize the result
    print(start,end,k)
    return min_val

def vitre(N, k):
    tab = [[[0] * (k + 1) for _ in range(N + 1)]for _ in range(N+1)]

   # for i in range(1, N + 1):
    #    for j in range(1, N + 1):
     #       for p in range(1, k+1):
      #          tab[i][j][p] = calcul_value(i, j, p, tab)
    tab[1][N][k] = calcul_value(1,N,k,tab) # on n'a pas besoin de calculer tous les elements du tab,
                                                # il faut juste calculer les donnees(sous-questions) besoins
    print(tab[1][N])
    return tab[1][N][k]


#Fonction main, vous ne devriez pas avoir à modifier
#Main function, you shouldn't have to modify it
def main(args):
    N = int(args[0])
    k = int(args[1])

    answer = vitre(N,k)
    print(answer)

if __name__ == '__main__':
    main(sys.argv[1:])