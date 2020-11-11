
from dataclasses import dataclass, field

def mineLeftToRightUpDown(mineGrid):
    opimalMineCumSum = [ [ 0 for j in range(len(mineGrid[0])) ] for i in range(len(mineGrid)) ]

    for j in range(len(mineGrid[0])):
        for i in range(len(mineGrid)):
            if j == 0:
                opimalMineCumSum[i][j] = mineGrid[i][j]
            else:
                opimalMineCumSum[i][j] = mineGrid[i][j] + max(
                    opimalMineCumSum[i-1][j-1] if i-1 >= 0 else 0,
                    opimalMineCumSum[i][j-1],
                    opimalMineCumSum[i+1][j-1] if i+1 < len(opimalMineCumSum) else 0
                )

    return max([opimalMineCumSum[i][len(mineGrid)-1] for i in range(len(mineGrid))])


@dataclass
class AggregateNode(object):

    endingMax : int = 1
    lengths : list = field(default_factory=list)
    nodes : list = field(default_factory=list)

    def add(self, i, j, length):
        self.nodes.append((i, j))
        self.lengths.append(length)
        self.endingMax = max(length, self.endingMax)


def longestSnake(snakeGrid):

    #A snake sequence is made up of adjacent numbers in the grid such that for each number, the number on the right or the
    #number below it is +1 or -1 its value. For example, if you are at location (x, y) in the grid,
    #you can either move right i.e. (x, y+1) if that number is ± 1 or move down i.e. (x+1, y) if that number is ± 1.

    def _checkIfValidNodeUp(i, j):
        if i-1 >= 0 and abs(snakeGrid[i][j] - snakeGrid[i-1][j]) == 1:
            return True
        return False

    def _checkIfValidNodeLeft(i, j):
        if j-1 >= 0 and abs(snakeGrid[i][j] - snakeGrid[i][j-1]) == 1:
            return True
        return False

    optimalLongestSnake = [ [ AggregateNode(1) for j in range(len(snakeGrid[0])) ] for i in range(len(snakeGrid))  ]
    maxNodeSoFar = (1, 1)
    maxLengthSoFar = 1

    for i in range(len(snakeGrid)):
        for j in range(len(snakeGrid[0])):
            aggNode = optimalLongestSnake[i][j]
            if _checkIfValidNodeUp(i, j):
                aggNode.add(i-1, j, optimalLongestSnake[i-1][j].endingMax+1)

            if _checkIfValidNodeLeft(i, j):
                aggNode.add(i, j-1, optimalLongestSnake[i][j-1].endingMax+1)

            if aggNode.endingMax > maxLengthSoFar:
                maxLengthSoFar = aggNode.endingMax
                maxNodeSoFar = (i, j)

    return maxLengthSoFar
