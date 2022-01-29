
class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLL:

    def __init__(self):
        self.l = 0
        self.head = None
        self.end = None

    def insert_at_front(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.end = n
        else:
            self.head.prev = n
            n.next = self.head
            self.head = n
        self.l += 1
        return n

    def delete(self, node):
        pre = node.prev
        nex = node.next
        if pre:
            pre.next = nex
        else:
            self.head = nex

        if nex:
            nex.prev = pre
        else:
            self.end = pre
        self.l -= 1

    def delete_end_node(self):
        res = self.end
        pre = self.end.prev
        if pre:
            pre.next = None
            self.end = pre
        else:
            self.head = None
        self.l -= 1
        return res


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        res = self.cache[key]
        self.dll.delete(res[1])
        n = self.dll.insert_at_front(key)
        self.cache[key] = (res[0], n)
        return res[0]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            res = self.cache[key]
            self.dll.delete(res[1])
            n = self.dll.insert_at_front(key)
            self.cache[key] = (value, n)
        else:
            if self.dll.l == self.capacity:
                n = self.dll.delete_end_node()
                self.cache.pop(n.val)

            n = self.dll.insert_at_front(key)
            self.cache[key] = (value, n)
