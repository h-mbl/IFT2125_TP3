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
        print("Do Something")

class Algorithm1(Strategy) :
    def __init__(self, width, height):
        super().__init__()
        #la longueur & la hauteur
        self.width = width
        self.height = height
        # enregistre le mur et le trou
        self.grid = [[1 for _ in range(width)] for _ in range(height)]
        # enregistre les elements visites en true
        self.visited = [[False for _ in range(width)] for _ in range(height)]
        a = 0

    def backtracker(self, x, y):
        # ici,on cherhce les elements non-visites de notre element actuel
        neighbors = self.get_unvisited_neighbors(x, y)
        # si la liste est vide, ce qu'on a visite tous les elements proches
        if not neighbors:
            return

        # on choisit aleatoirement  l'element qui sera place comme visite dans la liste des voisns
        nx, ny = random.choice(neighbors)
        # on supprimer le mur
        self.remove_wall(x, y, nx, ny)
        self.visited[ny][nx] = True
        # on fait une reccursion
        self.backtracker(nx, ny)

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
        #Si les cellules sont horizontalement adjacentes (x == nx),
        # cela signifie qu'il y a un mur horizontal entre elles.
        #Dans ce cas, la fonction met à 0 (supprime le mur) dans la grille aux positions [y][x] et [ny][nx].
        # Cela crée un passage horizontal entre les deux cellules.
        if x == nx:
            self.grid[y][x] = 0
            self.grid[ny][nx] = 0
        #Si les cellules sont verticalement adjacentes (x != nx), cela signifie qu'il y a un mur vertical entre elles.
        #Dans ce cas, la fonction met à 0 (supprime le mur) dans la grille aux positions [y][x] et [y][nx].
        #Cela crée un passage vertical entre les deux cellules.
        else:
            self.grid[y][x] = 0
            self.grid[y][nx] = 0

    def Apply(self):
        # Forcer la première ligne (y = 0)
        start_y = 0
        # Choisir une colonne aléatoire
        start_x = random.randint(0, self.width - 1)
        # on change l'element comme True dans le tableau visited
        self.visited[start_y][start_x] = True
        # on appelle la fonction backtracker avec les starts elements
        self.backtracker(start_x, start_y)
        print("Applying Algorithm1")
        self.export_maze_to_scad('maze.scad', self.width, self.height)

    def export_maze_to_scad(self, filename, maze_width, maze_height, wall_width=10, wall_height=10):
        try:
            with open(filename, 'w') as f:
                f.write("difference() {\n")  # Début de l'opération de différence
                f.write("union() {\n")  # Début de l'union des murs

                # Base plate
                f.write("translate([-0.5, -0.5, -1]) {\n")
                f.write("cube([{}, {}, 1], center=false);\n".format(maze_width * wall_width + 1,
                                                                    maze_height * wall_height + 1))
                f.write("}\n")

                # Murs du labyrinthe
                for y in range(maze_height):
                    for x in range(maze_width):
                        if self.grid[y][x] == 1:  # Cellule = mur
                            f.write("translate([{}, {}, 0]) {{\n".format(x * wall_width, y * wall_height))
                            f.write("cube([{}, {}, {}], center=true);\n".format(wall_width, wall_width, wall_height))
                            f.write("}\n")

                f.write("}\n")  # Fin de l'union des murs

                # Bordures extérieures
                f.write("translate([-0.5, -0.5, 0]) {\n")
                f.write("cube([{}, 1, {}], center=false);\n".format(maze_width * wall_width + 1, wall_height))
                f.write("cube([1, {}, {}], center=false);\n".format(maze_height * wall_height + 1, wall_height))
                f.write(f"translate([{maze_width * wall_width}, 0, 0]) " "{\n")
                f.write("cube([1, {}, {}], center=false);\n".format(maze_height * wall_height + 1, wall_height))
                f.write("}\n")
                f.write(f"translate([0, {maze_height * wall_height}, 0])" "{\n")
                f.write("cube([{}, 1, {}], center=false);\n".format(maze_width * wall_width + 1, wall_height))
                f.write("}\n")
                f.write("}\n")  # Fin des bordures extérieures

                # Logo
                f.write("// Logo\n")
                f.write("translate([1, -0.2, 1]) {\n")
                f.write("rotate([90, 0, 0]) {\n")
                f.write("linear_extrude(1) text(\"RM\", size=7.0);\n")
                f.write("}\n")
                f.write("}\n")

                f.write("}\n")  # Fin de l'opération de différence

            print(f"Labyrinthe exporté avec succès dans le fichier {filename}")
        except IOError:
            print(f"Erreur lors de l'écriture du fichier {filename}")
class Algorithm2(Strategy) :

    def Apply(self):
        #super().Apply()
        print("Applying Algorithm2")

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
        my_generator.SetStrategy(Algorithm1(13,13))
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
