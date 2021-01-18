import unittest
from challenges.src.datastructures import lists

class Test_List(unittest.TestCase):

    def test_lists(self):
        listOfLists = [
            lists.ListNode(1, lists.ListNode(2, lists.ListNode(3))),
            lists.ListNode(5, lists.ListNode(7, lists.ListNode(10))),
            lists.ListNode(2, lists.ListNode(3, lists.ListNode(5))),
            lists.ListNode(4, lists.ListNode(12, lists.ListNode(13)))
        ]
        res1 = []
        ll1 = lists.mergeKLists(listOfLists)
        while ll1:
            res1.append(ll1.val)
            ll1 = ll1.next

        res2 = []
        ll2 = lists.mergeKListsWithPriorityQueue(listOfLists)
        while ll2:
            res2.append(ll2.val)
            ll2 = ll2.next

        self.assertEquals(res1, res2)
        self.assertEquals(res1, [1, 2, 2, 3, 3, 4, 5, 5, 7, 10, 12, 13])
