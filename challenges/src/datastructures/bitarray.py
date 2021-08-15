
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

def longestConsecutive(self, nums: List[int]) -> int:
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

        pB = BitArray(max(nums))
        nB = BitArray(abs(min(nums)))
        zero = False
        for e in nums:
            if e < 0:
                nB.set(abs(e))
            elif e > 0:
                pB.set(e)
            else:
                nB.set(abs(e))
                pB.set(e)
                zero = True

        #print(pB.arr)
        #print(nB.arr)

        def maxCount(nums):
            mx = 0
            c = 0
            for i in nums:
                if i == '1':
                    c += 1
                    if mx < c:
                        mx = c
                else:
                    c = 0
            return mx


        st = ''
        ct = 0
        for e in nB.arr[::-1] + pB.arr:
            if e:
                st += str(bin(e)).replace('0b', '')
            else:
                ct = max(ct, maxCount(st))
                st = ''

        return ct-1 if zero else ct