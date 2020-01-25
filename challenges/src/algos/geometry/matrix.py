
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





