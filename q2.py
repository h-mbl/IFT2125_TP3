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
    print(matrice)
    # je dois creer un cadre
    nombreColonne = len(matrice[0])
    nombreLigne = len(matrice)

    elementVisite= []

    # au lieu de faire plein d'analyse je peux juste utiliser try and catch :
    i = 0
    j = 0
    global indexFirstLine,positionDernierElement, courtChemin
    positionElement=[]
    courtChemin = 0
    indexFirstLine = None

    while i < nombreLigne :
        # choisir la premiere place ou commencer
        if i == 0 and courtChemin == 0:
            # sauvegarder le resultat de la ligne
            firstLine =[]
            for j in range(nombreColonne):
                # en cherchant la position nous gerons notre cadre
                # le but est de verifie si la potentiel valeur sera hors de notre cadre
                positionhaut = j + nombreColonne
                positionGauche = j-1
                positionDroit = j+1

                # si la position < a 0 donc nous sommes en dehors de notre ligne par exemple pour (0,0)
                if positionGauche >= 0:
                    # nous cherchons les elements au tours de l'element,il y a try-catch
                    try : elementGauche = matrice[i][j-1]
                    except : elementGauche = 0
                else : elementGauche = 0

                if positionDroit < nombreColonne :
                    try: elementDroite = matrice[i][j+1]
                    except : elementDroite = 0
                else : elementDroite = 0

                if positionhaut < nombreLigne * nombreColonne:
                    try: elementHaut = matrice[i+1][j]
                    except : elementHaut = 0
                else : elementHaut = 0

                # on cherche le minimum de l'iteration
                minimum = 0
                tmp_minimum = [elementGauche, elementDroite, elementHaut]

                # la boucle permet d'ignorer les elements hors du cadre
                while minimum == 0 :
                    minimum = min(tmp_minimum)
                    if minimum == 0 :
                        index = tmp_minimum.index(0)
                        tmp_minimum.pop(index)
                    else :
                        firstLine.append(minimum + matrice[i][j])

            indexFirstLine = firstLine.index(min(firstLine))
            positionDernierElement = [i,indexFirstLine]
            elementVisite.append(f"{i}{indexFirstLine}")
            courtChemin += matrice[i][indexFirstLine]
        else :
            firstLine = []
            truei = positionDernierElement[0]
            truej = positionDernierElement[1]
            a = 0
            elementAnalyser =[]
            try :
                tmp = matrice[i][j - 1]
                if f"{i}{j-1}" not in elementVisite:
                    elementAnalyser.append(-1)
            except : pass

            try :
                tmp = matrice[i][j - 1]
                if f"{i}{j + 1}" not in elementVisite:
                    elementAnalyser.append(1)
            except : pass

            try :
                tmp = matrice[i+1][j]
                if f"{i+1}{j}" not in elementVisite:
                    elementAnalyser.append(2)
            except : pass

            for k in elementAnalyser :
                if k == 2 :
                    j =  positionDernierElement[1]
                    i = positionDernierElement[0] + 1
                else :
                    j = positionDernierElement[1] + k
                    i = positionDernierElement[0]

                positionhaut = j + nombreColonne
                positionGauche = j - 1
                positionDroit = j + 1
                if positionGauche >= 0:
                    try:
                        elementGauche = matrice[i][j - 1]
                        if i == truei and j-1 == truej:
                            elementGauche = 0
                    except: elementGauche = 0
                else: elementGauche = 0

                if positionDroit < nombreColonne:
                    try:
                        elementDroite = matrice[i][j + 1]
                        if i == truei and j + 1 == truej:
                            elementDroite = 0
                    except: elementDroite = 0
                else: elementDroite = 0

                if positionhaut < nombreLigne * nombreColonne:
                    try:  elementHaut = matrice[i + 1][j]
                    except: elementHaut = 0
                else: elementHaut = 0
                minimum = 0
                tmp_minimum = [elementGauche, elementDroite, elementHaut]
                while minimum == 0:
                    minimum = min(tmp_minimum)
                    if minimum == 0:
                        index = tmp_minimum.index(0)
                        tmp_minimum.pop(index)
                    else :
                        firstLine.append(minimum + matrice[i][j])
            a = 0
            index = firstLine.index(min(firstLine))
            if index == 0:
                positionDernierElement = [truei, truej - 1]
            elif index == 1:
                positionDernierElement = [truei, truej + 1]
            else:
                positionDernierElement = [truei + 1, truej]

            if f"{positionDernierElement[0]}{positionDernierElement[1]}" not in elementVisite :
                elementVisite.append(f"{positionDernierElement[0]}{positionDernierElement[1]}")
                courtChemin += matrice[positionDernierElement[0]][positionDernierElement[1]]
                print(positionDernierElement)
                print(courtChemin)
            else :
                tmp_firstLine = firstLine.copy()
                tmp_firstLine.pop(index)
                index = None
                while index == None:
                    minimum = (min(tmp_firstLine))
                    index = firstLine.index(minimum)
                    if index == 0:
                        positionDernierElement = [truei, truej - 1]
                    elif index == 1:
                        positionDernierElement = [truei, truej + 1]
                    else:
                        positionDernierElement = [truei + 1, truej]
                    elementVisite.append(f"{positionDernierElement[0]}{positionDernierElement[1]}")
                    print(positionDernierElement)
                    print(courtChemin)

            #breakpoint()
main("test.txt")