from dataclasses import dataclass

@dataclass
class Quack(object):

    arr1 : list
    arr2 : list
    arr3 : list
    total: int = 0

    def push(self, elem):
        self.arr1.append(elem)
        self.arr2.append(elem)
        self.total += 1

    def pop(self):
        if self.total == 0:
            del self.arr1[:]
            del self.arr3[:]
            raise Exception("Nothing to pop")
        
        if self.arr2:
            self.arr2.pop()
        self.total -= 1
        return self.arr1.pop()

    def pull(self):
        if self.total == 0:
            del self.arr1[:]
            del self.arr3[:]
            raise Exception("Nothing to pull")
        if len(self.arr3) == 0:
            while self.arr2:
                self.arr3.append(self.arr2.pop())
        self.total -= 1
        return self.arr3.pop()


        



