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
    width = 4
    height = 4
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
            print("new start")

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
                print(len(visited),len(unvisited))
                print(unvisited,pos,chemin,visited)


        print("result is")
        print(result)
        #le resultat est une liste des chemins passes qui combinent le labyrinth
        m = self.chemins2murs(result)
        print(m)
        return result

    def chemins2murs(self,chemins):
        map = dict()
        for chemin in chemins:
            last = chemin[0]

            for i in range(1,len(chemin)):

                curr = chemin[i]

                map[(last,curr)] =  0
                last = curr
            for x in range(self.width):
                for y in range(self.width):
                    if (x,y) not in map and (y,x) not in map:
                        map[(x,y)] = 1

        return map



    def Apply(self):
        #super().Apply()
        print("Applying Algorithm1")

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

