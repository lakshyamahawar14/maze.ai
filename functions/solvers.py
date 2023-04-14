import random


class Solvers:

    def backtrackingSolver(self, generatorObj):
        legal_edges = generatorObj.legal_edges
        starting_point = generatorObj.entry_exit_points[0]
        exits = generatorObj.entry_exit_points[1:]
        current = starting_point
        path = []
        seen = []
        while current not in exits:
            neighbors = [n for n in legal_edges[current] if n not in path]
            if len(neighbors) > 0:
                seen.append(current)
                path.append(current)
                random_neighbor = neighbors[random.randint(
                    0, len(neighbors)-1)]
                current = random_neighbor
            elif len(seen) > 0:
                path.append(current)
                current = seen.pop()
        path.append(current)
        seen.append(exits[0])
        return seen

    def toggleSolutionDisplayed(self):
        if (self.isSolutionDisplayed == False):
            self.isSolutionDisplayed = True
        else:
            self.isSolutionDisplayed = False

    def insertSolutionPath(self, solversObj, gameObj):
        solutionPath = solversObj.solutionPath
        for i in range(len(solutionPath)):
            x = solutionPath[i][0]
            y = solutionPath[i][1]
            index_i = gameObj.rowSize-x-1
            index_j = y
            gameObj.updateVisited((index_i, index_j), 1)

    def __init__(self):
        self.isSolutionDisplayed = False
        self.solutionPath = []
