global nombreColonne, nombreLigne,grandtableau

def main(path):
    matrice = []
    with open(path, 'r') as fichier:
        for ligne in fichier:  # Lire chaque ligne du fichier
            ligne_entiers = []  # Liste pour stocker les entiers de chaque ligne

            nombres = ligne.strip().split(
                ',')  # Séparer la ligne par les virgules et retirer les espaces autour des nombres

            for nombre in nombres:
                entier = int(nombre)  # Convertir la chaîne en entier
                ligne_entiers.append(entier)  # Ajouter l'entier à la liste de la ligne

            matrice.append(ligne_entiers)  # Ajouter la liste de la ligne à la matrice
    matrice = matrice[::-1]

    # je dois creer un cadre
    nombreColonne = len(matrice[0])
    nombreLigne = len(matrice)


    def case(i,tmp,tmp_cc):
        elementVisite = []
        courtChemin = tmp_cc
        positionDernierElement = tmp
        while i < nombreLigne:

            # enregistrer le vrai valeur de i et j
            i = positionDernierElement[0]
            j = positionDernierElement[1]

            tabposition=[]
            tabvaleur =[]

            for l in range(3):
                cas = [[0,-1],[0,1],[1,0]]
                z = cas[l]
                cas_i = z[0] + i
                cas_j = z[1] + j

                if cas_j >= 0 and cas_j < nombreColonne and cas_i < nombreLigne and [cas_i,  cas_j] not in elementVisite and cas_i > 0:

                    # definir le nouveau court chemin temporaire
                    tmp_courtChemin = courtChemin + matrice[cas_i][cas_j]

                    # dans notre tableau on place le court chemin temporaire
                    tableau[cas_i][cas_j] = tmp_courtChemin

                    tmp_visite =[]

                    while cas_i < i + 1:

                        # je prends l'element le plus minime qui me permettra d'escalader
                        tmp_element = []
                        tmp_position = []

                        # on verifie la droite
                        if cas_j + 1 < nombreColonne and [cas_i, cas_j + 1] not in elementVisite and cas_i > 0 and [cas_i, cas_j+1] not in tmp_visite:
                            tmp_element.append(tmp_courtChemin + matrice[cas_i][cas_j + 1])
                            tmp_position.append([cas_i,cas_j + 1])

                        # on verifie la gauche
                        if  cas_j - 1 >= 0 and [cas_i, cas_j - 1] not in elementVisite  and cas_i > 0 and [cas_i, cas_j-1] not in tmp_visite:
                            tmp_element.append(tmp_courtChemin + matrice[cas_i][cas_j - 1])
                            tmp_position.append([cas_i,cas_j - 1])

                        # on verifie en haut
                        if cas_i + 1 < nombreLigne and [cas_i + 1, cas_j] not in elementVisite and [cas_i + 1, cas_j] not in tmp_visite :
                            tmp_element.append(tmp_courtChemin + matrice[cas_i + 1][cas_j])
                            tmp_position.append([cas_i + 1,cas_j])

                        if len(tmp_element) > 0:
                            minimum = min(tmp_element)
                            tmp_nouvelle_position = tmp_position[tmp_element.index(minimum)]
                            cas_i = tmp_nouvelle_position[0]
                            cas_j = tmp_nouvelle_position[1]
                            tableau[cas_i][cas_j] = minimum
                            tmp_visite.append([cas_i,cas_j])
                            tmp_courtChemin = minimum
                    tabposition.append([cas_i,cas_j])
                    tabvaleur.append(tableau[cas_i][cas_j])

            index = tabvaleur.index(min(tabvaleur))
            nouveauI,nouveauJ = tabposition[index]
            elementVisite.append([nouveauI,nouveauJ])
            courtChemin = tableau[nouveauI][nouveauJ]
            positionDernierElement[0] = nouveauI
            positionDernierElement[1] = nouveauJ
            if nouveauI + 1 == nombreLigne:
                print(elementVisite)
                return courtChemin

    if nombreLigne <= 1:
        courtChemin = min(matrice[0])
        return courtChemin

    grandtableau = []
    for j in range(nombreColonne):
        if j == 2:
            a = 0
        # je cree une matrice vide
        tableau = [[0 for x in range(nombreColonne)] for x in range(nombreLigne)]
        elementVisite = []
        i = 0
        tableau[i][j] = matrice[1][j] + matrice[0][j]

        positionDernierElement = [0, j]

        elementVisite.append([i, j])
        courtChemin = matrice[0][j]
        tmp_courtChemin = case(i,positionDernierElement,courtChemin)
        grandtableau.append(tmp_courtChemin)
    print(min(grandtableau))
    print(grandtableau)

#main("C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt")
main("test.txt")