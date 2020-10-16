
def islandPerimeter(matrix):
    '''
        :param matrix:2D matrix of 1s and 0s where 1 represents land and 0 represents water.
    '''
    perimeter = 0
    for i, row in enumerate(matrix):
        for j, elem in enumerate(row):
            if elem == 1:
                for ni, nj in [(i, j-1), (i, j+1), (i+1, j), (i-1, j)]:
                    if (ni >= len(matrix)) or (ni < 0) or (nj >= len(matrix[0])) or (nj < 0) or matrix[ni][nj] == 0:
                        perimeter += 1
    return perimeter


def numberOfIslands(matrix):
    nx = [-1, -1, -1, 0, 0, 1, 1, 1]
    ny = [-1, 0, 1, -1, 1, -1, 0, 1]

    def _isWithinBounds(r, c):
        return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[0])

    def _dfs(i, j):
        visited[i][j] = True
        for x in nx:
            for y in ny:
                if _isWithinBounds(i+x, i+y) and (matrix[i+x][i+y] == 1) and (not visited[i+x][i+y]):
                    _dfs(i+x, i+y)

    visited = [[False]*len(matrix[0]) for _ in range(len(matrix))]
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (matrix[i][j] == 1 and not visited[i][j]):
                _dfs(i, j)
                count += 1
    return count






