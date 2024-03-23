# Fonction pour remplir les nombres avec des espaces si leur longueur est inférieure à 4
def remplir_espaces(nombre):
    if len(nombre) < 4:
        return ' ' * (4 - len(nombre)) + nombre
    else:
        return nombre

# Lecture du fichier texte
with open('test.txt', 'r') as fichier:
    lignes = fichier.readlines()

# Traitement et réécriture des lignes avec les nombres formatés
with open('test.txt', 'w') as nouveau_fichier:
    for ligne in lignes:
        nombres = ligne.strip().split(',')
        nouveaux_nombres = [remplir_espaces(nombre) for nombre in nombres]
        nouvelle_ligne = ', '.join(nouveaux_nombres)
        nouveau_fichier.write(nouvelle_ligne + '\n')