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

            # sinon,
            if True:
                # enregistrer le vrai valeur de i et j
                i = positionDernierElement[0]
                j = positionDernierElement[1]

                # si je vais a gauche
                gauche_position = []
                if j - 1 >= 0 and [i, j - 1] not in elementVisite and i > 0:

                    # definir le nouveau court chemin temporaire
                    tmp_courtChemin = courtChemin + matrice[i][j - 1]

                    # dans notre tableau on place le court chemin temporaire
                    tableau[i][j - 1] = tmp_courtChemin

                    # ajouter a la liste des elements de gauche
                    gauche_position.append([i, j - 1])

                    # on cree des gestionnaires de i et j temporaire
                    tmp_i = i
                    tmp_j = j - 1

                    # aussi longtemps que nous n'avons pas passer a la nouvelle ligne
                    while tmp_i < i + 1:

                        # je prends l'element le plus minim qui me permettra d'escalader
                        tmp_element = []
                        tmp_position = []

                        # j'ai un nouveau court chemin
                        tmp_courtChemin = tableau[tmp_i][tmp_j]

                        # on verifie la droite
                        if tmp_j + 1 < nombreColonne and [i, tmp_j + 1] not in elementVisite and [i,
                                                                                                  tmp_j + 1] not in gauche_position and tmp_i > 0:
                            tmp_element.append(tmp_courtChemin + matrice[i][tmp_j + 1])
                            tmp_position.append([tmp_i, tmp_j + 1])

                        # on verifie la gauche
                        if tmp_j - 1 >= 0 and [i, tmp_j - 1] not in elementVisite and [i,
                                                                                       tmp_j - 1] not in gauche_position and tmp_i > 0:
                            tmp_element.append(tmp_courtChemin + matrice[i][tmp_j - 1])
                            tmp_position.append([tmp_i, tmp_j - 1])

                        # on verifie en haut
                        if tmp_i + 1 < nombreLigne and [tmp_i + 1, tmp_j] not in gauche_position:
                            tmp_element.append(tmp_courtChemin + matrice[i + 1][tmp_j])
                            tmp_position.append([tmp_i + 1, tmp_j])

                        # on prends le minimum
                        minimum = min(tmp_element)

                        # on cherche l'index de 3 cote
                        indextab = tmp_element.index(minimum)
                        tmp = tmp_position[indextab]

                        # on a notre nouveau tmp_i et tmp_j
                        tmp_i = tmp[0]
                        tmp_j = tmp[1]
                        tableau[tmp_i][tmp_j] = minimum

                        # on enregistre dans le cas si nous allons a gauche
                        gauche_position.append([tmp_i, tmp_j])

                # si je vais a droite
                droite_position = []

                if j + 1 < nombreColonne and [i, j + 1] not in elementVisite and i > 0:
                    tmp_courtChemin = courtChemin + matrice[i][j + 1]

                    # dans notre tableau on place le court chemin temporaire
                    tableau[i][j + 1] = tmp_courtChemin

                    droite_position.append([i, j + 1])
                    # on cree des gestionnaires de i et j temporaire

                    tmp_i = i
                    tmp_j = j + 1

                    # aussi longtemps que nous n'avons pas passer a la nouvelle ligne
                    while tmp_i < i + 1:

                        # je prends l'element le plus minim qui me permettra d'escalader
                        tmp_element = []
                        tmp_position = []
                        # j'ai un nouveau court chemin
                        tmp_courtChemin = tableau[tmp_i][tmp_j]

                        # on verifie la droite
                        if tmp_j + 1 < nombreColonne and [i, tmp_j + 1] not in elementVisite and tmp_i > 0 and [i,
                                                                                                                tmp_j + 1] not in droite_position:
                            tmp_element.append(tmp_courtChemin + matrice[i][tmp_j + 1])
                            tmp_position.append([tmp_i, tmp_j + 1])

                        # on verifie la gauche
                        if tmp_j - 1 >= 0 and [i, tmp_j - 1] not in elementVisite and tmp_i > 0 and [i,
                                                                                                     tmp_j - 1] not in droite_position:
                            tmp_element.append(tmp_courtChemin + matrice[i][tmp_j - 1])
                            tmp_position.append([tmp_i, tmp_j - 1])

                        # on verifie en haut
                        if tmp_i + 1 < nombreLigne and [tmp_i + 1, tmp_j] not in droite_position:
                            tmp_element.append(tmp_courtChemin + matrice[i + 1][tmp_j])
                            tmp_position.append([tmp_i + 1, tmp_j])

                        # on prends le minimum
                        minimum = min(tmp_element)

                        # on cherche l'index de 3 cote
                        indextab = tmp_element.index(minimum)
                        tmp = tmp_position[indextab]

                        # on a notre nouveau tmp_i et tmp_j
                        tmp_i = tmp[0]
                        tmp_j = tmp[1]
                        tableau[tmp_i][tmp_j] = minimum

                        # on enregistre dans le cas si nous allons a droite
                        droite_position.append([tmp_i, tmp_j])

                # haut position
                haut_position = []
                if i + 1 < nombreLigne:
                    tmp_courtChemin = courtChemin + matrice[i + 1][j]

                    # dans notre tableau on place le court chemin temporaire
                    tableau[i + 1][j] = tmp_courtChemin

                    haut_position.append([i + 1, j])

                cas = [gauche_position, droite_position, haut_position]
                nom_cas = ["gauche", "droite", "haut"]
                poids = [0, 0, 0]
                retirer = []

                for x in range(3):
                    actuel_cas = cas[x]
                    tmp_courtChemin = courtChemin
                    for y in range(len(actuel_cas)):  # tmp_courtChemin = tableau[liste[0]][liste[1]]
                        liste = actuel_cas[y]
                        tmp_courtChemin = tableau[liste[0]][liste[1]]
                    poids[x] = tmp_courtChemin
                    if poids[x] == courtChemin:
                        retirer.append(nom_cas[x])
                tmp_poids = poids.copy()
                tmp_nom_cas = nom_cas.copy()

                for z in range(len(retirer)):
                    indexAsupprimer = tmp_nom_cas.index(retirer[z])
                    tmp_poids.pop(indexAsupprimer)
                    tmp_nom_cas.pop(indexAsupprimer)

                poids = tmp_poids
                nom_cas = tmp_nom_cas

                cas_le_moins_couteux = nom_cas[poids.index(min(poids))]

                # gauche
                if cas_le_moins_couteux == "gauche":
                    elementVisite = elementVisite + gauche_position
                    i = gauche_position[len(gauche_position) - 1][0]
                    j = gauche_position[len(gauche_position) - 1][1]
                    courtChemin = tableau[i][j]

                # droite
                elif cas_le_moins_couteux == "droite":
                    elementVisite = elementVisite + droite_position
                    i = droite_position[len(droite_position) - 1][0]
                    j = droite_position[len(droite_position) - 1][1]
                    courtChemin = tableau[i][j]

                # haut
                elif cas_le_moins_couteux == "haut":
                    elementVisite = elementVisite + haut_position
                    i = haut_position[len(haut_position) - 1][0]
                    j = haut_position[len(haut_position) - 1][1]
                    courtChemin = tableau[i][j]
                positionDernierElement[0] = i
                positionDernierElement[1] = j

                if i + 1 == nombreLigne:
                    return courtChemin

    if nombreLigne <= 1:
        courtChemin = min(matrice[0])
        return courtChemin
    grandtableau = []
    for j in range(nombreColonne):
        # je cree une matrice vide
        tableau = [[0 for x in range(nombreColonne)] for x in range(nombreLigne)]
        elementVisite = []
        i = 0
        tableau[i][j] = matrice[1][j] + matrice[1][j]

        positionDernierElement = [0, j]

        elementVisite.append([i, j])
        courtChemin = matrice[0][j]
        tmp_courtChemin = case(i,positionDernierElement,courtChemin)
        grandtableau.append(tmp_courtChemin)
    if 350639 in grandtableau:
        print("350639")
    print(min(grandtableau))
    print(grandtableau)






#main("C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt")
main("test.txt")