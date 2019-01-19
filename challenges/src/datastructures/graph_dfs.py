
def countIslands(adjMatrix):
    a = [-1, -1, -1, 0, 0, 1, 1, 1]
    b = [-1, 0, 1, 1, -1, -1, 0, 1]

    def isWithinBounds(i, j, rows, cols):
        return i >= 0 and j >= 0 and i < rows and j < cols

    def dfs(adjMatrix, i, j, visited, a, b, rows, cols):
        visited[i][j] = True
        for e1 in a:
            for e2 in b:
                x = i + e1
                y = j + e2
                if isWithinBounds(x, y, rows, cols) and not visited[x][y] and adjMatrix[x][y]:
                    dfs(adjMatrix, x, y, visited, a, b, rows, cols)

    rows = len(adjMatrix)
    cols = len(adjMatrix[0]) if rows else 0
    visited = [[False]*cols for i in range(0, rows)]
    islandCt = 0
    for i in range(rows):
        for j in range(cols):
            if adjMatrix[i][j] and not visited[i][j]:
                dfs(adjMatrix, i, j, visited, a, b, rows, cols)
                islandCt += 1
    return islandCt








