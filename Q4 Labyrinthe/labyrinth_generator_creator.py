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
    width = 3
    height = 3
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
        m = self.chemins2murs(result)
        code = self.translateMap2SCAD(m)
        print(code)
        return result

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
        print(m)
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
                        print(p1,p2)


                elif (p2,p1) in m:
                    if m[(p2,p1)] == 1:
                        result += self.murGeneration(p1,p2)
                        print(p1,p2)





        print(result)
    def murGeneration(self,p1,p2):

        rotation = self.rotationOrNot(p1, p2)
        rotation = rotation * 90
        x = ((p1[0]+1) + (p2[0] +1)) / 2
        y = ((p1[1] +1) + (p2[1] +1))/ 2
        result = "translate([%f, %f, %f]){rotate([0,0,%f]){cube([%f,1,%f], center = true);} } \n" % (
        cell_size * x, cell_size * y, wall_height / 2, rotation, cell_size + wall_thickness, wall_height)
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

    def backtracker(self, x, y):
        # Marquer la cellule actuelle comme visitée
        self.visited[y][x] = True
        self.stack.append((x, y))  # Utilisez stack pour le backtracking
        # Ajouter la cellule actuelle au chemin
        self.chemin.append((x, y))

        while self.chemin:
            try:
                x, y = self.stack[-1]  # Utiliser la dernière position dans le chemin
            except:break
            neighbors = self.get_unvisited_neighbors(x, y)

            if not neighbors:
                # Si aucun voisin non visité, reculer
                self.stack.pop()
            else:
                # Choisir un voisin au hasard parmi les non visités
                nx, ny = random.choice(neighbors)
                # Supprimer le mur entre la cellule actuelle et le voisin choisi
                self.remove_wall(x, y, nx, ny)
                # Marquer le voisin comme visité et l'ajouter au chemin
                self.stack.append((nx, ny))
                self.visited[ny][nx] = True
                self.chemin.append((nx, ny))

        # Une fois tous les chemins explorés, générer la sortie SCAD
        m = self.chemins2murs2(self.chemin)
        self.translateMap2SCAD(m)

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

    def chemins2murs2(self,resultat):
        resultat_map = {}
        for x in range(self.width):
            for y in range(self.height):
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        resultat_map[(x, y), (nx, ny)] = int(
                            ((x, y), (nx, ny)) not in resultat and ((nx, ny), (x, y)) not in resultat)
        return resultat_map

    def translateMap2SCAD(self, resultat_map):
        result = "translate([-0.5,-0.5,-1]) cube([{}, {}, 1]);\n".format(self.height * cell_size + 1,
                                                                         self.width * cell_size + 1)
        milieu_width = self.width * cell_size / 2
        milieu_height = self.height * cell_size / 2

        # Construire les murs extérieurs
        wall_commands = [
            f"translate([0, {milieu_height + cell_size / 2}, {cell_size / 2}]){{rotate([0,0,90]){{cube([{self.height * cell_size + 1 - cell_size},1,{wall_height}], center = true);}}}}",
            f"translate([{cell_size * self.height}, {milieu_height}, {cell_size / 2}]){{rotate([0,0,90]){{cube([{self.height * cell_size + 1},1,{wall_height}], center = true);}}}}",
            f"translate([{milieu_width}, 0, {cell_size / 2}]){{cube([{self.height * cell_size + 1},1,{wall_height}], center = true);}}",
            f"translate([{milieu_width}, {cell_size * self.width}, {cell_size / 2}]){{cube([{self.height * cell_size + 1},1,{wall_height}], center = true);}}"
        ]
        result += "\n".join(wall_commands) + "\n"

        # Ajouter les murs intérieurs
        for (x1, y1), (x2, y2) in resultat_map.keys():
            if resultat_map[(x1, y1), (x2, y2)] == 1:
                rotation = self.rotationOrNot((x1, y1,), (x2, y2)) * 90
                x = (x1 + x2) * cell_size / 2
                y = (y1 + y2) * cell_size / 2
                result += f"translate([{x}, {y}, {wall_height / 2}]){{rotate([0,0,{rotation}]){{cube([{cell_size + 1},1,{wall_height}], center = true);}}}}\n"

        print("-----------------------------")
        print(result)
        breakpoint()
        return result

    def rotationOrNot(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        if dx == 1 and dy == 0:
            # Les cellules sont horizontalement adjacentes
            return False
        elif dx == 0 and dy == 1:
            # Les cellules sont verticalement adjacentes
            return True
        else:
            raise ValueError(f"Les cellules {p1} et {p2} ne sont pas adjacentes.")

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

