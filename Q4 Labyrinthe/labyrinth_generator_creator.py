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

