
def nQueens(n, board=[]):

    def isValid(board, curcol):
        currow = len(board)-1
        for row, col in enumerate(board[:-1]):
            if col == curcol or currow - row == abs(curcol-col):
                return False
        return True

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




