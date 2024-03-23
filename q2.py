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


    K = [[0 for x in range(nombreColonne )] for x in range(nombreLigne )]

    #breakpoint()
    elementVisite= []

    # au lieu de faire plein d'analyse je peux juste utiliser try and catch :
    i = 0
    j = 0
    global indexFirstLine, courtChemin, positionDernierElement
    positionElement=[]
    courtChemin = 0
    indexFirstLine = None

    while i < nombreLigne :
        # choisir la premiere place ou commencer
        if i == 0 and courtChemin == 0:
            # sauvegarder le resultat de la ligne
            firstLine =[]
            if nombreLigne == 1 :
                courtChemin += min(matrice[0])
                print(courtChemin)
                break
            for j in range(nombreColonne):
                # en cherchant la position nous gerons notre cadre
                # le but est de verifie si la potentiel valeur sera hors de notre cadre
                positionhaut = j + nombreColonne
                positionGauche = j-1
                positionDroit = j+1

                element=[]
                # si la position < a 0 donc nous sommes en dehors de notre ligne par exemple pour (0,0)
                if positionGauche >= 0:
                    # nous cherchons les elements au tours de l'element,il y a try-catch
                    try :
                        elementGauche = matrice[i][j-1]
                        element.append(elementGauche)
                    except : pass
                else : pass

                if positionDroit < nombreColonne :
                    try:
                        elementDroite = matrice[i][j+1]
                        element.append(elementDroite)
                    except : pass
                else : pass

                if positionhaut < nombreLigne * nombreColonne:
                    try:
                        elementHaut = matrice[i+1][j]
                        element.append(elementHaut)
                    except : pass
                else : pass

                # on cherche le minimum de l'iteration
                # la boucle permet d'ignorer les elements hors du cadre
                minimum = min(element)
                firstLine.append(minimum + matrice[i][j])

            indexFirstLine = firstLine.index(min(firstLine))
            positionDernierElement = [i,indexFirstLine]
            elementVisite.append(f"{i}{indexFirstLine}")
            courtChemin += matrice[i][indexFirstLine]
        else :
            firstLine = []
            truei = positionDernierElement[0]
            truej = positionDernierElement[1]


            elementAnalyser =[]
            element =[]
            try :
                tmp = matrice[truei][truej - 1]
                if f"{truei}{truej-1}" not in elementVisite and truej-1 >= 0:
                    elementAnalyser.append(-1)
                else: elementAnalyser.append("None")
            except: elementAnalyser.append("None")


            try :
                tmp = matrice[truei][truej - 1]
                if f"{truei}{truej + 1}" not in elementVisite and truej-1 >= 0:
                    elementAnalyser.append(1)
                else : elementAnalyser.append("None")
            except : elementAnalyser.append("None")

            try :
                tmp = matrice[truei+1][truej]
                if f"{truei+1}{truej}" not in elementVisite and truei+1 < nombreLigne:
                    elementAnalyser.append(2)
                else: elementAnalyser.append("None")
            except: elementAnalyser.append("None")

            for k in elementAnalyser :


                if  k == "None" :
                    firstLine.append(10000000)
                    continue

                elif k == 2 :
                    j =  positionDernierElement[1]
                    i = positionDernierElement[0] + 1

                else :
                    j = positionDernierElement[1] + k
                    i = positionDernierElement[0]
                if j >= nombreColonne or i >= nombreLigne  :
                    firstLine.append(10000000)
                    continue
                positionhaut = j + nombreColonne
                positionGauche = j - 1
                positionDroit = j + 1
                if positionGauche >= 0:
                    try:
                        if i == truei and j - 1 == truej:
                            pass
                        else :
                            elementGauche = matrice[i][j - 1]
                            element.append(elementGauche)
                    except: pass
                else: pass

                if positionDroit < nombreColonne:
                    try:
                        elementDroite = matrice[i][j + 1]
                        if i == truei and j + 1 == truej:
                            pass
                        else : element.append(elementDroite)
                    except: pass
                else: pass

                if positionhaut < nombreLigne * nombreColonne:
                    try:
                        elementHaut = matrice[i + 1][j]
                        element.append(elementHaut)
                    except: pass
                else: pass

                try : minimum = min(element)
                except:
                    minimum = None
                    break
                firstLine.append(minimum + matrice[i][j])

            try :
                if len(element) > 0:
                    index = firstLine.index(min(firstLine))
                else :
                    pass
            except: break
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
            if truei == 2 and truej == 0:
                pass
            if positionDernierElement[0] + 1 >= nombreLigne:
                break
            #breakpoint()
main("C:/Users/herve/OneDrive/Documents/GitHub/IFT2125_TP3/Q2 Escalade/wall5.txt")
#main("test.txt")