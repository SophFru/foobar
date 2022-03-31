#I used breadth first search to solve this challenge

def solution(map):
    def removable(i, j):
        count = 0
        foo = [-1, 0, 1, 0]
        bar = list(reversed(foo))
        for (a, b) in zip(foo, bar):
            x = i + a
            y = j + b
            if isValid(x, y, len(map), len(map[0])):
                if map[x][y] == 0:
                    count += 1
        return count < 2

    #preprocess walls
    removableWalls = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1 and not removable(i, j):
                removableWalls.append((i, j))

    minDist = len(map) + len(map[0]) - 1

    shortPath = bfs(map)
    if shortPath and minDist == shortPath:
        return shortPath
    else:
        shortPath = len(map) * len(map[0])
        while removableWalls:
            currWall = removableWalls.pop()
            map[currWall[0]][currWall[1]] = 0
            temp = bfs(map)
            if temp:
                if temp == minDist:
                    return temp
                elif temp < shortPath:
                    shortPath = temp
            map[currWall[0]][currWall[1]] = 1
        return shortPath

def isValid(x, y, w, h):
    inLowerBound = x > -1 and y > -1
    inUpperBound = x < w and y < h
    return inLowerBound and inUpperBound

def bfs(map):
    foo = [-1, 0, 1, 0]
    bar = list(reversed(foo))
    visited = [[False for j in range(len(map[0]))] for i in range(len(map))]
    q = []
    start = Node(0, 0, 1)
    q.append(start)
    visited[0][0] = True
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                visited[i][j] = True
    while q:
        curr = q.pop(0)
        if curr.x == len(map) - 1 and curr.y == len(map[0]) - 1:
            return curr.dist
        for (a,b) in zip(foo,bar):
            x = curr.x + a
            y = curr.y + b
            if isValid(x, y, len(map), len(map[0])) and not visited[x][y]:
                q.append(Node(x, y, curr.dist + 1))
                visited[x][y] = True

class Node:
    def __init__(self, x, y, dist):
        self.x = x
        self.y = y
        self.dist = dist

    