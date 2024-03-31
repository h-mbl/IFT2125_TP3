def main(path) :
    def element_doublon_et_valeur(tableau):
        elements_vus = set()  # Un ensemble pour stocker les éléments déjà rencontrés

        for element in tableau:
            if element in elements_vus:
                return element  # Retourne l'élément en double
            else:
                elements_vus.add(element)  # Sinon, ajoutez-le à l'ensemble

        return None  # Si aucun élément n'est en double, retournez None

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
            # 0, 40
            # enregistrer le vrai valeur de i et j
            # Nous ne calculerons pas toutes les lignes de la matrice pour que l'algo soit optimal
            truei = positionDernierElement[0]
            truej = positionDernierElement[1]

            # pour trouver le prochain element,on doit chercher la difficulte des elements proches de notre
            # trueJ and trueI

            for k in range(3):
                element = []
                # gauche,droite,haut selon k
                cas = [[0,-1],[0,1],[1,0]]
                l = cas[k][0]
                m = cas[k][1]

                # on a le nouveau i and j
                i = positionDernierElement[0] + l
                j = positionDernierElement[1] + m

                # 0n est oblige de recalculer a chaque fois car si une valeur
                #if (i < nombreLigne and j < nombreColonne) and tableau[i][j] == 0 :

                # on calcule la difficulte des elements proches
                if (i < nombreLigne and j < nombreColonne) and tableau[i][j] == 0 :

                    if j-1 >= 0 and  f"{i} {j-1}" not in elementVisite:
                            element.append(matrice[i][j-1])

                            for tmp_k in range(3):
                                tmp_element = []
                                # gauche,droite,haut selon k
                                tmp_cas = [[0, -1], [0, 1], [1, 0]]
                                tmp_l = tmp_cas[tmp_k][0]
                                tmp_m = tmp_cas[tmp_k][1]

                                # on a le nouveau i and j
                                tmp_i = i + tmp_l
                                tmp_j = j + tmp_m

                                # on calcule la difficulte des elements proches
                                if (tmp_i < nombreLigne and tmp_j < nombreColonne) and tableau[tmp_i][tmp_j] == 0:
                                    if tmp_j - 1 >= 0 and f"{tmp_i} {tmp_j - 1}" not in elementVisite:
                                        tmp_element.append(matrice[tmp_i][tmp_j - 1])

                                    if tmp_j + 1 < nombreColonne and f"{tmp_i} {tmp_j + 1}" not in elementVisite:
                                        element.append(matrice[tmp_i][tmp_j + 1])
                                    if tmp_i + 1 < nombreLigne:
                                        tmp_element.append(matrice[tmp_i + 1][tmp_j])
                                    # par exemple a la derniere ligne,c'est probable qu'on ait ce cas.
                                    if len(tmp_element) == 0:
                                        continue
                                    tmp_minimum = min(tmp_element)
                                    tableau[tmp_i][tmp_j] = tmp_minimum + matrice[tmp_i][tmp_j]
                                else:
                                    continue
                    if j+1 < nombreColonne  and f"{i} {j+1}" not in elementVisite:
                            element.append(matrice[i][j+1])

                            for tmp_k in range(3):
                                tmp_element = []
                                # gauche,droite,haut selon k
                                tmp_cas = [[0, -1], [0, 1], [1, 0]]
                                tmp_l = tmp_cas[tmp_k][0]
                                tmp_m = tmp_cas[tmp_k][1]

                                # on a le nouveau i and j
                                tmp_i = i + tmp_l
                                tmp_j = j + tmp_m

                                # on calcule la difficulte des elements proches
                                if (tmp_i < nombreLigne and tmp_j < nombreColonne) and tableau[tmp_i][tmp_j] == 0:
                                    if tmp_j - 1 >= 0 and f"{tmp_i} {tmp_j - 1}" not in elementVisite:
                                        tmp_element.append(matrice[tmp_i][tmp_j - 1])

                                    if tmp_j + 1 < nombreColonne and f"{tmp_i} {tmp_j + 1}" not in elementVisite:
                                        element.append(matrice[tmp_i][tmp_j + 1])
                                    if tmp_i + 1 < nombreLigne:
                                        tmp_element.append(matrice[tmp_i + 1][tmp_j])
                                    # par exemple a la derniere ligne,c'est probable qu'on ait ce cas.
                                    if len(tmp_element) == 0:
                                        continue
                                    tmp_minimum = min(tmp_element)
                                    tableau[tmp_i][tmp_j] = tmp_minimum + matrice[tmp_i][tmp_j]
                                else:
                                    continue

                    if i + 1 < nombreLigne :
                        element.append(matrice[i+1][j])

                        for tmp_k in range(3):
                            tmp_element = []
                            # gauche,droite,haut selon k
                            tmp_cas = [[0, -1], [0, 1], [1, 0]]
                            tmp_l = tmp_cas[tmp_k][0]
                            tmp_m = tmp_cas[tmp_k][1]

                            # on a le nouveau i and j
                            tmp_i = i + tmp_l
                            tmp_j = j + tmp_m

                            # on calcule la difficulte des elements proches
                            if (tmp_i < nombreLigne and tmp_j < nombreColonne) and tableau[tmp_i][tmp_j] == 0:
                                if tmp_j - 1 >= 0 and f"{tmp_i} {tmp_j - 1}" not in elementVisite:
                                    tmp_element.append(matrice[tmp_i][tmp_j - 1])

                                if tmp_j + 1 < nombreColonne and f"{tmp_i} {tmp_j + 1}" not in elementVisite:
                                    element.append(matrice[tmp_i][tmp_j + 1])
                                if tmp_i + 1 < nombreLigne:
                                    tmp_element.append(matrice[tmp_i + 1][tmp_j])
                                # par exemple a la derniere ligne,c'est probable qu'on ait ce cas.
                                if len(tmp_element) == 0:
                                    continue
                                tmp_minimum = min(tmp_element)
                                tableau[tmp_i][tmp_j] = tmp_minimum + matrice[tmp_i][tmp_j]
                            else:
                                continue

                    # par exemple a la derniere ligne,c'est probable qu'on ait ce cas.
                    if len(element) == 0 :
                       continue
                    minimum = min(element)
                    tableau[i][j] = minimum + matrice[i][j]
                else:
                    continue

            tmp_position =[]
            element = []
            autreElement = []
            tmp_autreElement = []
            autreElement_position = []
            tmp_autreElement_position = []
            # gauche
            if truej - 1 >= 0 and f"{truei} {truej-1}" not in elementVisite and truei > 0:
                element.append(tableau[truei][truej - 1])
                tmp_position.append([truei,truej - 1])

                #Autre element
                # gauche
                if truej - 1 - 1 >= 0 and f"{truei} {truej - 1 - 1 }" not in elementVisite and truei > 0:
                    tmp_autreElement.append(tableau[truei][truej - 1 -1])
                    tmp_autreElement_position.append([truei,truej-1-1])

                # droite
                #if truej + 1 - 1 < nombreColonne and f"{truei} {truej + 1 - 1}" not in elementVisite and truei > 0:
                #    tmp_autreElement.append(tableau[truei][truej + 1 - 1])
                #    tmp_autreElement_position.append([truei,truej + 1 - 1])

                # haut
                if truei + 1 <= nombreLigne and truej - 1 >= 0:
                    tmp_autreElement.append(tableau[truei+1][truej - 1])
                    tmp_autreElement_position.append([truei + 1, truej -1])

            if len(tmp_autreElement) > 0 :
                autreElement.append(tmp_autreElement)
                autreElement_position.append(tmp_autreElement_position)

            tmp_autreElement = []
            tmp_autreElement_position = []

            # droite
            if truej + 1 < nombreColonne and f"{truei} {truej+1}" not in elementVisite and truei > 0 :
                tmp_position.append([truei,truej + 1])
                element.append(tableau[truei][truej + 1])

                # Autre element
                # gauche
                #if truej + 1 - 1 >= 0 and f"{truei} {truej +  1 - 1}" not in elementVisite and truei > 0:
                #    tmp_autreElement.append(tableau[truei][truej + 1 - 1])
                #   tmp_autreElement_position.append([truei, truej + 1 - 1])

                # droite
                if truej + 1 +  1 < nombreColonne and f"{truei} {truej + 1 + 1}" not in elementVisite and truei > 0:
                    tmp_autreElement.append(tableau[truei][truej + 1 + 1])
                    tmp_autreElement_position.append([truei, truej + 1 + 1])

                # haut
                if truei + 1  <= nombreLigne and truej + 1 >= 0 :
                    tmp_autreElement.append(tableau[truei + 1][truej + 1])
                    tmp_autreElement_position.append([truei + 1, truej + 1])
            if len(tmp_autreElement) > 0 :
                autreElement.append(tmp_autreElement)
                autreElement_position.append(tmp_autreElement_position)

            tmp_autreElement = []
            tmp_autreElement_position = []

            #haut
            if i + 1 <= nombreLigne :
                tmp_position.append([truei+1,truej])
                element.append(tableau[truei + 1][truej])

                # Autre element
                # haut
                if i + 1 + 1 <= nombreLigne:
                    tmp_autreElement.append(tableau[truei + 1 + 1][truej])
                    tmp_autreElement_position.append([truei + 1 + 1, truej])

            if len(tmp_autreElement) > 0 :
                autreElement.append(tmp_autreElement)
                autreElement_position.append(tmp_autreElement_position)

            # si aucun element n'est disponible c'est probable qu'on soit deja a la fin du tableau
            if len(element) == 0 :
                return courtChemin
            # ceci permet de ne pas considere le cote qui sont deja visite
            while True:
                # si il y a des elements avec la meme difficulte vaut mieux monter qu'aller a cote ainsi ceci permet
                # d'enlever tout le doublon
                # gauche - droite - haut
                breakpoint()
                minimum = min(element)
                indextab = element.index(minimum)
                if f"{tmp_position[indextab][0]} {tmp_position[indextab][1]}" in elementVisite :
                    element.pop(element.index(minimum))
                    tmp_position.pop(indextab)
                else :
                    break
            tableau[truei][truej] = minimum
            courtChemin +=  matrice[tmp_position[indextab][0]][tmp_position[indextab][1]]
            positionDernierElement = [tmp_position[indextab][0],tmp_position[indextab][1]]
            elementVisite.append(f"{tmp_position[indextab][0]} {tmp_position[indextab][1]}")
            if positionDernierElement[0] + 1 >= nombreLigne :
                print(elementVisite[-1])
                print(courtChemin)
                #breakpoint()
                return courtChemin
            print(elementVisite[-1])
            print(courtChemin)

main("./wall1.txt")
#main("test.txt")