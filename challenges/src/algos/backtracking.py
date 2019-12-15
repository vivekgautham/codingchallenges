from dataclasses import dataclass

def nQueens(n, board=[]):

    def isValid(board, curcol):
        currow = len(board)-1
        for row, col in enumerate(board[:-1]):
            if col == curcol or currow - row == abs(curcol-col):
                return False
        return True

    if n == 0:
        return 0
    if len(board) == n:
        return 1
    count = 0
    for col in range(n):
        board.append(col)

        if isValid(board, col):
            count += nQueens(n, board)
        board.pop()
    return count

def itinerary(flights, curItin):
    if not flights:
        return curItin
    lastStop = curItin[-1]
    for i, (origin, dest) in enumerate(flights):
        curItin.append(dest)
        if origin == lastStop:
            return itinerary(flights[:i]+flights[i+1:], curItin)
        curItin.pop()
    return None

def sumSubset(array, s):
    allSubs = []

    def _sumSubSetRec(array, s, st, sub=[]):
        if sum(sub) == s:
            allSubs.append([e for e in sub])
        for i in range(st, len(array)):
            sub.append(array[i])
            if sum(sub) <= s:
                _sumSubSetRec(array, s, i+1, sub)
            sub.pop()

    _sumSubSetRec(array, s, 0)
    return allSubs

@dataclass
class SudokuSolver():

    board : list
    emptyVal : int = 0

    def _getFirstEmptyRowCol(self):
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                if self.board[row][col] == self.emptyVal:
                    return row, col
        return None, None

    def _isValidSoFar(self):
        if not self._rowsValid():
            return False
        if not self._colsValid():
            return False
        if not self._blocksValid():
            return False
        return True

    def _rowsValid(self):
        for row in self.board:
            if self._duplicates(row):
                return False
        return True

    def _colsValid(self):
        for col in map(list, zip(*self.board)):
            if self._duplicates(col):
                return False
        return True

    def _blocksValid(self):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                data = []
                for l in range(i, i+3):
                    for m in range(j, j+3):
                        data.append(self.board[l][m])
                if self._duplicates(data):
                    return False
        return True

    def _duplicates(self, l):
        s = set()
        for each in l:
            if each in s:
                return True
            if each != self.emptyVal:
                s.add(each)
        return False

    def _isComplete(self):
        return self._isValidSoFar() and all([all([each != self.emptyVal for each in row]) for row in self.board])

    def solve(self):
        row, col = self._getFirstEmptyRowCol()
        if row is None:
            return
        for num in range(1, 10):
            self.board[row][col] = num
            if self._isValidSoFar():
                self.solve()
                if self._isComplete():
                    return self.board
            self.board[row][col] = self.emptyVal


