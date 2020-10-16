from challenges.src.datastructures.stack import MinHeap

class HuffmanNode:

    def __init__(self, symbol, frequency, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency

    def __repr__(self):
        return self.symbol + ' : ' + str(self.frequency)

    def __str__(self):
        return self.symbol + ' : ' + str(self.frequency)

class HuffmanTree:

    def __init__(self, symbols, frequencies):
        self.symbols = symbols
        self.frequencies = frequencies
        self.minheap = MinHeap([])

        for symbol, freq in zip(self.symbols, self.frequencies):
            self.minheap.push(HuffmanNode(symbol, freq))

        while (len(self.minheap.heaparray) > 1):
            el1 = self.minheap.pop()
            el2 = self.minheap.pop()
            self.minheap.push(HuffmanNode('*', el1.frequency + el2.frequency, left=el1, right=el2))

        self.codes = {}

    def _computeRecurse(self, node, code=None, start=0):
        code = code or ''
        if (node.left):
            self._computeRecurse(node.left, code=code+'0', start=start+1)
        if (node.right):
            self._computeRecurse(node.right, code=code+'1', start=start+1)

        if (not node.left and not node.right):
            print('{0} : {1}'.format(node.symbol, code))
            self.codes[node.symbol] = code

    def computeCodes(self):
        self._computeRecurse(self.minheap.heaparray[0])






