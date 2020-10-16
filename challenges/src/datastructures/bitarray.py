
class BitArray:

    def __init__(self, n):
        self.arr = [0] * ((n >> 5) + 1)

    def get(self, pos):
        index = pos >> 5
        bitNo = pos & 31
        return (self.arr[index] & (1 << bitNo)) != 0

    def set(self, pos):
        index = pos >> 5
        bitNo = pos & 31
        self.arr[index] |= (1 << bitNo)

def checkDuplicates(arr, numberOfElements=1000):
    ba = BitArray(numberOfElements)
    dupes = False
    for num in arr:
        if ba.get(num):
            dupes = True
            break
        else:
            ba.set(num)
    return dupes