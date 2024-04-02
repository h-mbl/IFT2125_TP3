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

    tableau = [[0 for x in range(nombreColonne )] for x in range(nombreLigne )]

    elementVisite= []
    global indexFirstLine, courtChemin, positionDernierElement
    i=0
    courtChemin = 0
    indexFirstLine = None
    while i < nombreLigne:
        # choisir la premiere place ou commencer
        if i == 0 and courtChemin == 0:
            if nombreLigne == 1 :
                courtChemin += min(matrice[0])
                break
            for j in range(nombreColonne):
                element = []
                if j-1 >= 0 :
                    element.append(matrice[i][j-1])
                if j+1 < nombreColonne :
                    element.append(matrice[i][j+1])
                if j + nombreColonne < nombreLigne * nombreColonne :
                    element.append(matrice[i+1][j])
                minimum = min(element)
                tableau[i][j] = minimum + matrice[i][j]
            indexFirstLine = tableau[0].index(min(tableau[0]))
            positionDernierElement = [i,indexFirstLine]
            courtChemin += matrice[0][indexFirstLine]
        else :
            # 0, 40
            truei = positionDernierElement[0]
            truej = positionDernierElement[1]

            for k in range(3):
                element = []

                cas = [[0,-1],[0,1],[1,0]]
                l = cas[k][0]
                m = cas[k][1]

                i = positionDernierElement[0] + l
                j = positionDernierElement[1] + m


                if (i < nombreLigne and j < nombreColonne) and tableau[i][j] == 0:
                    if truei == 2 and truej == 40:
                        a = 0
                    if j-1 >= 0 and f"{i} {j-1}" not in elementVisite:
                        element.append(matrice[i][j-1])
                    if j+1 < nombreColonne and f"{i} {j+1}" not in elementVisite:
                        element.append(matrice[i][j+1])
                    if i + 1 < nombreLigne :
                        element.append(matrice[i+1][j])
                    if len(element) == 0 and i:
                       # print(courtChemin)
                       # return courtChemin
                        continue
                    minimum = min(element)
                    tableau[i][j] = courtChemin + matrice[i][j]
                else : continue

            tmp_position =[]
            element = []
            if truej - 1 >= 0 and f"{i} {truej-1}" not in elementVisite and truei > 0:
                element.append(tableau[truei][truej - 1])
                tmp_position.append([truei,truej - 1])
            if truej + 1 < nombreColonne and f"{i} {truej+1}" not in elementVisite and truei > 0 :
                tmp_position.append([truei,truej + 1])
                element.append(tableau[truei][truej + 1])
            if i + 1 <= nombreLigne  :
                tmp_position.append([truei+1,truej])
                element.append(tableau[truei + 1][truej])
            if len(element) == 0 :
                #print(courtChemin)
                #return courtChemin
                pass
            while True:
                try :
                    minimum = min(element)
                except :
                    print(courtChemin)
                    return courtChemin
                indextab = element.index(minimum)
                if f"{tmp_position[indextab][0]} {tmp_position[indextab][1]}" in elementVisite :
                    element.pop(element.index(minimum))
                    tmp_position.pop(indextab)
                else :
                    break
            tableau[truei][truej] = minimum #+ matrice[tmp_position[indextab][0]][tmp_position[indextab][1]]
            courtChemin +=  matrice[tmp_position[indextab][0]][tmp_position[indextab][1]]
            positionDernierElement = [tmp_position[indextab][0],tmp_position[indextab][1]]
            elementVisite.append(f"{tmp_position[indextab][0]} {tmp_position[indextab][1]}")
            if positionDernierElement[0] + 1 >= nombreLigne :
                print(elementVisite[-1])
                print(courtChemin)
                breakpoint()
                return courtChemin
            print(elementVisite[-1])
            print(courtChemin)
            print("---------")


main("C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt")
#main("test.txt")