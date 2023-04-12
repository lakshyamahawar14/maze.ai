import numpy as np
import random


class KruskalMaze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes, self.edges = self.createGraph()
        self.maze = self.generateGrid()
        self.maze_edges = self.maze
        self.legal_edges = self.getLegalTraversalEdges()
        self.entry_exit_points, self.entry_exit_edges = self.getEntryExits()
        self.maze_data = self.getMazeWalls()

    def get_random_edge_weights(self):
        edge_weights = [(random.randint(1, 4), x, y) for (x, y) in self.edges]
        return edge_weights

    def getLegalTraversalEdges(self):
        legal_edges = {}
        for s in sorted(self.maze):
            if s[0] not in legal_edges:
                legal_edges[s[0]] = [s[1]]
            else:
                legal_edges[s[0]].append(s[1])
            if s[1] not in legal_edges:
                legal_edges[s[1]] = [s[0]]
            else:
                legal_edges[s[1]].append(s[0])
        return legal_edges

    def createGraph(self):
        x = self.width
        y = self.height
        nodes = set()
        edges = set()
        for i in range(x):
            for j in range(y):
                nodes.add((i, j))
                if i > 0:
                    e1 = (i-1, j)
                    edges.add(((i, j), e1))
                if i < x-1:
                    e2 = (i+1, j)
                    edges.add(((i, j), e2))
                if j > 0:
                    e3 = (i, j-1)
                    edges.add(((i, j), e3))
                if j < y-1:
                    e4 = (i, j+1)
                    edges.add(((i, j), e4))
        return nodes, edges

    def generateGrid(self):
        edge_weights = self.get_random_edge_weights()
        clusters = {n: n for n in self.nodes}
        ranks = {n: 0 for n in self.nodes}
        solution = set()

        def find(u):
            if clusters[u] != u:
                clusters[u] = find(clusters[u])
            return clusters[u]

        def union(x, y):
            x, y = find(x), find(y)
            if ranks[x] > ranks[y]:
                clusters[y] = x
            else:
                clusters[x] = y
            if ranks[x] == ranks[y]:
                ranks[y] += 1

        for w, x, y in sorted(edge_weights):
            if x != y:
                if find(x) != find(y):
                    # add edge to solution
                    solution.add((x, y))
                    union(x, y)
        return solution

    def getEdgeLocations(self):
        edge_data = []
        for edge in sorted(self.maze_edges):
            e1 = edge[0]
            e2 = edge[1]
            if e1[0] == e2[0]:
                if e1[1] > e2[1]:
                    # left edge
                    edge_data.append([[e1[1], e1[1]], [e1[0]+1, e1[0]]])
                else:
                    # right edge
                    edge_data.append([[e1[1]+1, e1[1]+1], [e1[0], e1[0]+1]])
            if e1[1] == e2[1]:
                if e1[0] > e2[0]:
                    # need a top edge
                    edge_data.append([[e1[1], e1[1]+1], [e1[0], e1[0]]])
                else:
                    # bottom edge
                    edge_data.append([[e1[1]+1, e1[1]], [e1[0]+1, e1[0]+1]])
        edge_data.extend(self.entry_exit_edges)
        return edge_data

    def getMazeWalls(self):
        edge_data = self.getEdgeLocations()
        maze_data = []
        for i in range(self.height):
            for j in range(self.width):
                top_edge = [[j, j+1], [i, i]]
                if top_edge in edge_data:
                    pass
                elif [[j+1, j], [i, i]] in edge_data:
                    pass
                else:
                    # print("edge between ", "(", j, ", ", i, ")",
                    #       " and ", "(", j+1, ", ", i, ")")
                    maze_data.append([(j, i), (j+1, i)])
                bottom_edge = [[j+1, j], [i+1, i+1]]
                if bottom_edge in edge_data:
                    pass
                elif [[j, j+1], [i+1, i+1]] in edge_data:
                    pass
                else:
                    # print("edge between ", "(", j+1, ", ", i+1, ")",
                    #       " and ", "(", j, ", ", i+1, ")")
                    maze_data.append([(j+1, i+1), (j, i+1)])
                right_edge = [[j+1, j+1], [i, i+1]]
                if right_edge in edge_data:
                    pass
                elif [[j+1, j+1], [i+1, i]] in edge_data:
                    pass
                else:
                    # print("edge between ", "(", j+1, ", ", i, ")",
                    #       " and ", "(", j+1, ", ", i+1, ")")
                    maze_data.append([(j+1, i), (j+1, i+1)])
                left_edge = [[j, j], [i+1, i]]
                if left_edge in edge_data:
                    pass
                elif [[j, j], [i, i+1],] in edge_data:
                    pass
                else:
                    # print("edge between ", "(", j, ", ", i, ")",
                    #       " and ", "(", j, ", ", i+1, ")")
                    maze_data.append([(j, i), (j, i+1)])
        return maze_data

    def getEntryExits(self):
        entry_exit_edge_data = []
        p1 = (0, random.randint(0, self.width-1))
        half_h = self.height // 2
        p2 = (random.randint(half_h, self.height-1), 0)
        p3 = (self.height-1, (random.randint(0, self.height-1)))
        half_w = self.width // 2
        p4 = (random.randint(half_w, self.width-1), self.height-1)
        entry_exit_edge_data.append(
            [[p1[1], p1[1]+1], [p1[0], p1[0]]])  # bottom edge
        entry_exit_edge_data.append(
            [[p2[1], p2[1]], [p2[0]+1, p2[0]]])  # left edge
        entry_exit_edge_data.append(
            [[p3[1], p3[1]+1], [p3[0]+1, p3[0]+1]])  # top edge
        entry_exit_edge_data.append(
            [[p4[1]+1, p4[1]+1], [p4[0], p4[0]+1]])  # right edge
        # squares of entry/exit locations
        self.entry_exit_points = [p1, p2, p3, p4]
        return self.entry_exit_points, entry_exit_edge_data


class Generators:
    def generateRandom(self, size):
        row = 2*size[0]-1
        col = 2*size[1]-1
        levelMatrix = [[0 for i in range(col)] for j in range(row)]

        for i in range(row):
            for j in range(col):
                if i % 2 == 0 and j % 2 == 0:
                    levelMatrix[i][j] = 0
                elif i % 2 == 1 and j % 2 == 1:
                    levelMatrix[i][j] = -1
                else:
                    p = 0.60
                    levelMatrix[i][j] = np.random.choice([0, 1], p=[p, 1-p])

        return levelMatrix
    
    def transformMazeData(self, size, mazeData):
        row = 2*size[0]-1
        col = 2*size[1]-1
        levelMatrix = [[0 for i in range(col)] for j in range(row)]
        for i in range(len(mazeData)):
            edge = mazeData[i]
            x1 = edge[0][0]
            y1 = edge[0][1]
            x2 = edge[1][0]
            y2 = edge[1][1]

            if x1 == x2 and x1 == 0:
                continue
            elif y1 == y2 and y1 == size[0]:
                continue
            elif x1 == x2 and x1 == size[1]:
                continue
            elif y1 == y2 and y1 == 0:
                continue
            else:
                if x1 == x2:
                    x = 2*(size[0]-max(y1, y2))
                    y = 2*x1-1
          
                    levelMatrix[x][y] = 1
                else:
                    x = 2*(size[0]-y1)-1
                    y = 2*min(x1, x2)
          
                    levelMatrix[x][y] = 1

        for i in range(row):
            for j in range(col):
                if i % 2 == 0 and j % 2 == 0:
                    levelMatrix[i][j] = 0
                elif i % 2 == 1 and j % 2 == 1:
                    levelMatrix[i][j] = -1

        return levelMatrix


    def generateKruskalMaze(self, size):
        mazeData = KruskalMaze(size[0], size[1]).maze_data
        levelMatrix = self.transformMazeData(size, mazeData)
        return levelMatrix

    def findUniquePathsHelper(self, i, j, r, c, levelMatrix):
        if (i == r or j == c):
            return 0
        if (levelMatrix[i][j] != 0):
            return 0
        if (i == r-1 and j == c-1):
            return 1
        return self.findUniquePathsHelper(i+1, j, r, c, levelMatrix) + self.findUniquePathsHelper(i, j+1, r, c, levelMatrix)

    def findUniquePaths(self, levelMatrix):
        r, c = len(levelMatrix), len(levelMatrix[0])
        return self.findUniquePathsHelper(0, 0, r, c, levelMatrix)

    def generateManual(self, gameObj):
        rowSize = gameObj.rowSize
        colSize = gameObj.colSize
        size = (rowSize, colSize)
        gameObj.startNewGame(size)

    def generateLevel(self, size):
        levelMatrix = []
        countpaths = 0
        while (True):
            levelMatrix = self.generateKruskalMaze(size)
            countpaths = self.findUniquePaths(levelMatrix)
            if (countpaths != 0):
                break
        countones = 0
        for i in range(size[0]):
            for j in range(size[1]):
                countones += levelMatrix[i][j] == 1
        self.generateKruskalMaze(size)
        return (levelMatrix, countpaths, countones)

    def __init__(self):
        pass
