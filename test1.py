def main(path) :

    matrice = []
    with open(path, 'r') as fichier:
        for ligne in fichier:  # Lire chaque ligne du fichier
            ligne_entiers = []  # Liste pour stocker les entiers de chaque ligne

            nombres = ligne.strip().split(',')  # Séparer la ligne par les virgules et retirer les espaces autour des nombres

            for nombre in nombres:
                entier = int(nombre)  # Convertir la chaîne en entier
                ligne_entiers.append(entier)  # Ajouter l'entier à la liste de la ligne

            matrice.append(ligne_entiers)  # Ajouter la liste de la ligne à la matrice
    matrice = matrice[::-1]

    # je dois creer un cadre
    nombreColonne = len(matrice[0])
    nombreLigne = len(matrice)

    # je cree une matrice vide
    tableau = [[0 for x in range(nombreColonne )] for x in range(nombreLigne )]
    print(matrice[0][56]+ matrice[1][56])
    #print()

    print(matrice[0][40] + matrice[1][40])

    # enregistre les elements visites (en cpp ca sera plutot un ensemble)
    elementVisite= []

    global indexFirstLine, courtChemin, positionDernierElement
    i=0
    courtChemin = 0
    indexFirstLine = None
    while i < nombreLigne:
        # choisir la premiere place ou commencer (on cherche la premiere etape)
        if i == 0 and courtChemin == 0:
            # si il n'y a qu'un seule ligne alors le plus petit devient le plus court chemin
            if nombreLigne == 1 :
                courtChemin += min(matrice[0])
                break
            # sinon,pour chaque element de la ligne on cherche sa difficulte
            # j evolue selon for j in range cependant le i n'a pas besoin de bouger car nous sommes a la premiere
            # ligne
            for j in range(nombreColonne):
                element = []
                # gauche
                if j-1 >= 0 :
                    element.append(matrice[i][j-1])
                # droite
                if j+1 < nombreColonne :
                    element.append(matrice[i][j+1])
                # haut
                if i + 1 < nombreLigne :
                    element.append(matrice[i+1][j])
                # difficulte
                minimum = min(element)
                tableau[i][j] = minimum + matrice[i][j]
            # on cherche la difficulte la plus basse de cet index
            indexFirstLine = tableau[0].index(min(tableau[0]))
            # tableau == matrice
            positionDernierElement = [i,indexFirstLine]
            # on ajoute aux elements visite
            elementVisite.append(f"{i} {indexFirstLine}")
            # on incremente le plus court chemin
            courtChemin += matrice[0][indexFirstLine]
        # sinon,
        else :
            truei = positionDernierElement[0]
            truej = positionDernierElement[1]

            for k in range(8):
                cas = [[0, -1], [0, 1], [1, 0],[0,-2],[1,-1],[1,1],[0,2],[2,0]]
                l = cas[k][0]
                m = cas[k][1]

                # on a le nouveau i and j
                i = positionDernierElement[0] + l
                j = positionDernierElement[1] + m

                for n in range(3) :
                    element = []

                    # gauche,droite,haut selon k
                    cas = [[0, -1], [0, 1], [1, 0]]
                    tmp_l = cas[n][0]
                    tmp_m = cas[n][1]

                    # on a le nouveau i and j
                    tmp_i = i + tmp_l
                    tmp_j = j + tmp_m

                    if (tmp_i < nombreLigne and tmp_j < nombreColonne) :
                        if tmp_j - 1 >= 0 and f"{tmp_i} {tmp_j - 1}" not in elementVisite:
                            element.append(matrice[tmp_i][tmp_j - 1])

                        if tmp_j + 1 < nombreColonne and f"{tmp_i} {tmp_j + 1}" not in elementVisite:
                            element.append(matrice[tmp_i][tmp_j + 1])

                        if tmp_i + 1 < nombreLigne:
                            element.append(matrice[tmp_i + 1][tmp_j])

                        # par exemple a la derniere ligne,c'est probable qu'on ait ce cas.
                        if len(element) == 0:
                            continue
                        minimum = min(element)
                        tableau[tmp_i][tmp_j] = minimum + matrice[tmp_i][tmp_j]
                    else:
                        continue

            groupeGauche = []
            groupeGauche_position = []
            groupeDroite = []
            groupeDroite_position = []
            groupeHaut = []
            groupeHaut_position = []
            tmp_position = []
            element = []

            #  ----- Groupe Principal ----- #

            # gauche
            if truej - 1 >= 0 and f"{truei} {truej - 1}" not in elementVisite and truei > 0:
                element.append(tableau[truei][truej - 1])
                tmp_position.append([truei, truej - 1])
                groupeGauche_position.append([truei, truej - 1])
            # droite
            if truej + 1 < nombreColonne and f"{truei} {truej + 1}" not in elementVisite and truei > 0:
                tmp_position.append([truei, truej + 1])
                element.append(tableau[truei][truej + 1])
                groupeDroite_position.append([truei, truej + 1])
            # haut
            if truei + 1 < nombreLigne:
                tmp_position.append([truei + 1, truej])
                element.append(tableau[truei + 1][truej])
                groupeHaut_position.append([truei + 1, truej])

            # ------ Groupe Secondaire ----- #
            if truej - 2 >= 0 and f"{truei} {truej - 2}" not in elementVisite and truei > 0:
                groupeGauche.append(tableau[truei][truej - 2])
                groupeGauche_position.append([truei,truej - 2])

            if truei + 1 < nombreLigne and truej - 1 < nombreColonne and f"{truei + 1} {truej - 1}" not in elementVisite and truei > 0:
                groupeGauche.append(tableau[truei+1][truej-1])
                groupeGauche_position.append([truei+1,truej-1])

            if truej + 2 < nombreColonne and f"{truei} {truej + 2}" not in elementVisite and truei > 0:
                groupeDroite.append(tableau[truei][truej + 2])
                groupeDroite_position.append([truei,truej + 2])

            if truei + 1 < nombreLigne and truej + 1 < nombreColonne and f"{truei + 1} {truej + 1}" not in elementVisite and truei > 0:
                groupeDroite.append(tableau[truei + 1][truej + 1])
                groupeDroite_position.append([truei + 1,truej + 1])

            if truei + 2 < nombreLigne:
                groupeHaut.append(tableau[truei + 2][truej])
                groupeHaut_position.append([truei + 2,truej])

            autreElement_position = groupeGauche_position + groupeDroite_position + groupeHaut_position
            autreElement = groupeGauche + groupeDroite + groupeHaut
            index_minimum = element.index(min(element))
            index_maximum = autreElement.index(max(autreElement))
            position_minimum = tmp_position[index_minimum]
            position_maximum = autreElement_position[index_maximum]
            trouver = False


            while trouver == False :
                for x in range(3):
                    cas = [groupeDroite,groupeGauche,groupeHaut]
                    if position_minimum in cas[0] and position_maximum in cas[0]:
                        element.pop(element.index(index_minimum))
                        tmp_position.pop(index_minimum)
                        index_minimum = element.index(min(element))
                        position_minimum = tmp_position[index_minimum]
                        trouver = False
                        break
                    elif x == 2 :
                        trouver = True
            courtChemin += matrice[tmp_position[index_minimum][0]][tmp_position[index_minimum][1]]
            positionDernierElement = [tmp_position[index_minimum][0], tmp_position[index_minimum][1]]
            elementVisite.append(f"{tmp_position[index_minimum][0]} {tmp_position[index_minimum][1]}")
            if positionDernierElement[0] + 1 >= nombreLigne :
                print(elementVisite[-1])
                print(courtChemin)
                return courtChemin
            i = positionDernierElement[0]
            print(elementVisite[-1])
            print(courtChemin)

main("C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt")
#main("test.txt")