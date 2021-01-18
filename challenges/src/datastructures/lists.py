

from queue import PriorityQueue

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


def mergeKLists(lists):
    finalList = []

    listPtrs = [e for e in lists]
    while True:
        minK = None
        curMin = None
        for idx, li in enumerate(listPtrs):
            if li:
                if curMin is None or li.val < curMin:
                    curMin = li.val
                    minK = idx

        if minK is not None:
            finalList.append(ListNode(val=listPtrs[minK].val))
            if len(finalList) > 1:
                finalList[-2].next = finalList[-1]
            listPtrs[minK] = listPtrs[minK].next
        else:
            break

    return finalList[0] if finalList else None


def mergeKListsWithPriorityQueue(lists):
    head = curr = ListNode(0)
    pq = PriorityQueue()

    for l in lists:
        if l:
            pq.put((l.val, l))

    while not pq.empty():
        val, node = pq.get()
        curr.next = ListNode(val)
        curr = curr.next
        node  = node.next
        if node:
            pq.put((node.val, node))

    return head.next




