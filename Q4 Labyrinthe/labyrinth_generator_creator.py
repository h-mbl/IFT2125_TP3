import sys
import random


cell_size = 10 #mm
wall_height = 10 #mm
wall_thickness = 1 #mm

strategy_choice = 1

class Strategy :
    def __init__(self):
        pass

    def Apply(self):
        print("Applying Abstract Strategy")

    def DoSomething(self):
        algo1 = Algorithm1()
        maze = algo1.initialisation()

        print("Do Something")

class Algorithm1(Strategy) :
    #widson's algorithm
    width = 13
    height = 13
    def adjacentCells(self,pos:(int,int)):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cellAdjacents = []

        x = pos[0]
        y = pos[1]
        for direction in directions:
            X = direction[0] + x
            Y = direction[1] + y
            if(X >= 0 and X < self.width  and
                    (Y >= 0 and Y < self.height)):
                cellAdjacents.append((X, Y))
        return cellAdjacents

    def getchemin(self, visited, start : (int,int)):
        chemin = [start]
        curr = start

        while True:
            adjacent = self.adjacentCells(curr)
            choix= random.choice(adjacent)

            if all(pos in chemin for pos in adjacent): # si on est dans un boucle infini, on recommence
                curr = start
                chemin = [start]
            elif choix in chemin: #si chemin loop, on refait le random
                continue

            elif choix in visited:
                chemin.append(choix)
                return chemin #condition fin

            elif choix not in visited:
                curr = choix
                chemin.append(choix) #on ajoute le randomWalk au chemin



    def initialisation(self):

        visited = set() #set des positions deja passes
        unvisited = []
        for w in range(self.width): #initialisation
            for h in range(self.height):
                pair = (w,h)
                unvisited.append(pair)

        start = (0,0)
        visited.add(start)
        result = []
        unvisited.remove(start)

        while len(unvisited) != 0 :


           # choix = random.choice(unvisited)
           # if(choix == start) : continue
            choix = random.choice(unvisited)
            chemin = self.getchemin(visited,choix)
            copy = chemin.copy()
            result.append(copy)
            chemin.pop()
            for pos in chemin:
                visited.add(pos)
                if pos in unvisited: unvisited.remove(pos)




        #le resultat est une liste des chemins passes qui combinent le labyrinth
        print(len(result))
        breakpoint()
        m = self.chemins2murs(result)
        print(len(m))
        breakpoint()

        code = self.translateMap2SCAD(m)
        print(code)
        return m

    def chemins2murs(self,chemins):
        m = dict()
        for chemin in chemins:
            last = chemin[0]


            for i in range(1,len(chemin)):

                curr = chemin[i]

                m[(last,curr)] = 0
                last = curr
            cases = []
        for x in range(self.width):
            for y in range(self.width):
                cases.append((x,y))
        for pos in cases:
            adjacent = self.adjacentCells(pos)
            for pos2 in adjacent:
                if (pos2,pos) not in m:
                    if (pos, pos2) not in m:

                        m[(pos,pos2)] = 1
        return m

    def rotationOrNot(self,p1,p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        if (x,y) == (1,0): return False
        elif (x,y) == (0,1): return True

    def translateMap2SCAD(self,m):
        #initialisation

        result = "" #codeSCAD

        result += "translate([-0.5,-0.5,-1]) cube(["+ str(self.height * cell_size +1)+',' + str(self.width * cell_size + 1)+ ", 1]); \n"
        # base
        milieu_width = self.width * cell_size/2
        milieu_height = self.height * cell_size/2
        # les 4 grand murs
        result += "translate([0, %f, %f]){rotate([0,0,90]){cube([%f,1,%f], center = true);}} \n" %(milieu_height+ cell_size/2, cell_size/2 ,  self.height * cell_size +1 - cell_size,wall_height)
        result += "translate([%f, %f, %f]){rotate([0,0,90]){cube([%f,1,%f], center = true);}} \n" % (cell_size*self.height,milieu_height, cell_size / 2, self.height * cell_size + 1, wall_height)
        result += "translate([%f, 0, %f]){cube([%f,1,%f], center = true);} \n" % (milieu_width, cell_size / 2, self.height * cell_size + 1, wall_height)
        result += "translate([%f, %f, %f]){cube([%f,1,%f], center = true);} \n" % (milieu_width, cell_size * self.width,cell_size/2, self.height * cell_size + 1, wall_height)

        cases = []
        for x in range(self.width):
            for y in range(self.height):
                cases.append((x,y))

        for p1 in cases:
            adjacent = self.adjacentCells(p1)
            for p2 in adjacent:


                if (p1,p2) in m:
                    if m[(p1,p2)] == 1:
                        result += self.murGeneration(p1,p2)



                elif (p2,p1) in m:
                    if m[(p2,p1)] == 1:
                        result += self.murGeneration(p1,p2)


        return result





    def murGeneration(self,p1,p2):

        rotation = self.rotationOrNot(p1, p2)
        rotation = rotation * 90

        if rotation != 0:
            result = "translate([%f, %f, %f]){rotate([0,0,%f]){cube([%f,1,%f], center = true);} } \n" % (
                (max(p1[1],p2[1]))*cell_size, p1[0] * cell_size+ cell_size/2, wall_height / 2, rotation, cell_size + wall_thickness, wall_height)
        else:
            result = "translate([%f, %f, %f]){rotate([0,0,%f]){cube([%f,1,%f], center = true);} } \n" % (
                p1[1] * cell_size + cell_size/2, max(p1[0],p2[0]) * cell_size , wall_height / 2, rotation,
                cell_size + wall_thickness, wall_height)

        return result


    def Apply(self):
        #super().Apply()
        print("Applying Algorithm1")

class Algorithm2(Strategy) :
    def __init__(self):
        super().__init__()
        # Définition de la longueur et la hauteur du labyrinthe
        self.width = 13
        self.height = 13
        # Initialisation de la grille avec des murs (représentés par 1) et des cases non visitées
        self.grid = [[1 for _ in range(self.width)] for _ in range(self.height)]
        # Initialisation de la matrice des cases visitées
        self.visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        # Initialisation du chemin avec le point de départ (0,0)
        self.chemin = [(0, 0)]
        self.stack = [(0, 0)]
    #""""

    def backtracker(self, x, y):
        # ici,on cherhce les elements non-visites de notre element actuel
        while True:
            neighbors = self.get_unvisited_neighbors(x, y)
            # si la liste est vide, ce qu'on a visite tous les elements proches
            if not neighbors:
                chemins = self.chercherbranche()
                m = self.chemins2murs(chemins)
                self.translateMap2SCAD(m)
                return 0

            # on choisit aleatoirement  l'element qui sera place comme visite dans la liste des voisns
            nx, ny = random.choice(neighbors)
            # on supprimer le mur
            self.remove_wall(x, y, nx, ny)
            self.visited[ny][nx] = True
            # on fait une reccursion
            self.chemin.append((nx,ny))
            self.backtracker(nx, ny)

    def branche_backtracker(self, x, y):
        # ici,on cherhce les elements non-visites de notre element actuel
        while True:
            neighbors = self.get_unvisited_neighbors(x, y)
            # si la liste est vide, ce qu'on a visite tous les elements proches
            if not neighbors:
                return self.tmp_chemin
            # on choisit aleatoirement  l'element qui sera place comme visite dans la liste des voisns
            nx, ny = random.choice(neighbors)
            # on supprimer le mur
            self.remove_wall(x, y, nx, ny)
            self.visited[ny][nx] = True
            # on fait une reccursion
            self.tmp_chemin.append((nx, ny))
            self.branche_backtracker(nx, ny)

    def chercherbranche(self):
        chemin_principal =[]

        #print(self.visited)
        for element in self.chemin :
            x,y = element
            self.tmp_chemin = [(x, y)]
            self.branche_backtracker(x,y)

            chemin_principal.append(self.tmp_chemin)


        unvisited = []
        for w in range(self.width):  # initialisation
            for h in range(self.height):
                pair = (w, h)
                unvisited.append(pair)
        while len(unvisited) > 0:

            flattened_list = [item for sublist in chemin_principal for item in sublist]
            for element in unvisited:
                if element in flattened_list:
                    unvisited.remove(element)
            for element in unvisited:
                x,y = element
                self.visited[y][x] = True
                self.tmp_chemin = [(x, y)]
                self.branche_backtracker(x, y)
                chemin_principal.append(self.tmp_chemin)

        connexion =[]
        for element in chemin_principal:
            if len(element) == 1:
                connexion.append(element)
                chemin_principal.remove(element)
        flattened_list = [item for sublist in connexion for item in sublist]
        ok = []
        for element in flattened_list :
            x,y = element
            tmp_chemin = [(x, y)]

            liste_adj = self.adjacentCells((x,y))
            for element in liste_adj :
                if element in connexion and element not in ok :
                    nx,ny = element
                    tmp_chemin.append((nx,ny))
                    ok.append((nx,ny))
            if len(tmp_chemin) > 0:
                chemin_principal.append(tmp_chemin)

        return chemin_principal

    def get_unvisited_neighbors(self, x, y):
        # enregistre les elements visites
        neighbors = []
        # droite, gauche, haut, bas
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # si l'element n'est pas visite et tous les autres cas, on ajoute l'elements a la liste des voisins
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.visited[ny][nx]:
                neighbors.append((nx, ny))
        # retourne la liste
        return neighbors

    def remove_wall(self, x, y, nx, ny):
        # Si les cellules sont horizontalement adjacentes (x == nx),
        # cela signifie qu'il y a un mur horizontal entre elles.
        # Dans ce cas, la fonction met à 0 (supprime le mur) dans la grille aux positions [y][x] et [ny][nx].
        # Cela crée un passage horizontal entre les deux cellules.
        if x == nx:
            self.grid[y][x] = 0
            self.grid[ny][nx] = 0
        # Si les cellules sont verticalement adjacentes (x != nx), cela signifie qu'il y a un mur vertical entre elles.
        # Dans ce cas, la fonction met à 0 (supprime le mur) dans la grille aux positions [y][x] et [y][nx].
        # Cela crée un passage vertical entre les deux cellules.
        else:
            self.grid[y][x] = 0
            self.grid[y][nx] = 0

    def Apply(self):
        print("Applying Algorithm2")
        # Forcer la première ligne (y = 0)
        a = 0
        start_y  = 0
        # Choisir une colonne aléatoire, apparement il doit aussi commencer par 0
        start_x = 0
        # on change l'element comme True dans le tableau visited
        self.visited[start_y][start_x] = True
        # on appelle la fonction backtracker avec les starts elements
        self.backtracker(start_x, start_y)
       # self.translateMap2SCAD('maze.scad', self.width, self.height)
    def adjacentCells(self,pos:(int,int)):
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cellAdjacents = []

        x = pos[0]
        y = pos[1]
        for direction in directions:
            X = direction[0] + x
            Y = direction[1] + y
            if (X >= 0 and X < self.width  and
                    (Y >= 0 and Y < self.height)):
                cellAdjacents.append((X, Y))
        return cellAdjacents
    def chemins2murs(self, chemins):
        m = dict()
        for chemin in chemins:
            last = chemin[0]

            for i in range(1, len(chemin)):
                curr = chemin[i]

                m[(last, curr)] = 0
                last = curr
            cases = []
        for x in range(self.width):
            for y in range(self.width):
                cases.append((x, y))
        for pos in cases:
            adjacent = self.adjacentCells(pos)
            for pos2 in adjacent:
                if (pos2, pos) not in m:
                    if (pos, pos2) not in m:
                        m[(pos, pos2)] = 1
        return m

    def translateMap2SCAD(self,m):
        #initialisation

        result = "" #codeSCAD

        result += "translate([-0.5,-0.5,-1]) cube(["+ str(self.height * cell_size +1)+',' + str(self.width * cell_size + 1)+ ", 1]); \n"
        # base
        milieu_width = self.width * cell_size/2
        milieu_height = self.height * cell_size/2
        # les 4 grand murs
        result += "translate([0, %f, %f]){rotate([0,0,90]){cube([%f,1,%f], center = true);}} \n" %(milieu_height+ cell_size/2, cell_size/2 ,  self.height * cell_size +1 - cell_size,wall_height)
        result += "translate([%f, %f, %f]){rotate([0,0,90]){cube([%f,1,%f], center = true);}} \n" % (cell_size*self.height,milieu_height, cell_size / 2, self.height * cell_size + 1, wall_height)
        result += "translate([%f, 0, %f]){cube([%f,1,%f], center = true);} \n" % (milieu_width, cell_size / 2, self.height * cell_size + 1, wall_height)
        result += "translate([%f, %f, %f]){cube([%f,1,%f], center = true);} \n" % (milieu_width, cell_size * self.width,cell_size/2, self.height * cell_size + 1, wall_height)

        cases = []
        for x in range(self.width):
            for y in range(self.height):
                cases.append((x,y))

        for p1 in cases:
            adjacent = self.adjacentCells(p1)
            for p2 in adjacent:


                if (p1,p2) in m:
                    if m[(p1,p2)] == 1:
                        result += self.murGeneration(p1,p2)



                elif (p2,p1) in m:
                    if m[(p2,p1)] == 1:
                        result += self.murGeneration(p1,p2)


        print(result)
        return result

    def rotationOrNot(self, p1, p2):
        x = abs(p1[0] - p2[0])
        y = abs(p1[1] - p2[1])
        if (x, y) == (1, 0):
            return False
        elif (x, y) == (0, 1):
            return True


    def murGeneration(self,p1,p2):

        rotation = self.rotationOrNot(p1, p2)
        rotation = rotation * 90

        if rotation != 0:
            result = "translate([%f, %f, %f]){rotate([0,0,%f]){cube([%f,1,%f], center = true);} } \n" % (
                (max(p1[1],p2[1]))*cell_size, p1[0] * cell_size+ cell_size/2, wall_height / 2, rotation, cell_size + wall_thickness, wall_height)
        else:
            result = "translate([%f, %f, %f]){rotate([0,0,%f]){cube([%f,1,%f], center = true);} } \n" % (
                p1[1] * cell_size + cell_size/2, max(p1[0],p2[0]) * cell_size , wall_height / 2, rotation,
                cell_size + wall_thickness, wall_height)

        return result


class Generator() :
    strategy = None

    def __init__(self):
        pass

    def SetStrategy(self, new_strategy):
        self.strategy = new_strategy

    def Generate(self):
        self.strategy.Apply()
        self.strategy.DoSomething()

class Creator() :
    def __init__(self):
        pass

    def PrintLabyrinth(self):
        pass


# main call
def main():
    global strategy_choice
    args = sys.argv[:]
    if len(args) >= 2 :
        strategy_choice = int(args[1])

    # Generator
    my_generator = Generator()
    if strategy_choice == 1:
        my_generator.SetStrategy(Algorithm1())
    elif strategy_choice == 2:
        my_generator.SetStrategy(Algorithm2())
    else :
        print("error strategy choice")
    my_generator.Generate()

    #Creator
    my_creator = Creator()
    my_creator.PrintLabyrinth()


if __name__ == "__main__":
    main()

