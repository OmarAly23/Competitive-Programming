# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def get_len(self, head):
        counter = 0
        tmp = head
        while tmp is not None:
            counter += 1
            tmp = tmp.next
        return counter

    def printL(self, head):
        tmp = head
        while tmp is not None:
            print(tmp.val)
            tmp = tmp.next

    def middleNode(self, head):
        length = self.get_len(head)
        if length % 2 == 0:
            ite = 0
            stopping_index = length/2
            tmp = head
            while tmp is not None:
                if stopping_index == ite:
                    return tmp
                tmp = tmp.next
                ite += 1
        else:
            ite = 0
            stopping_index = length//2
            tmp = head
            while tmp is not None:
                if stopping_index == ite:
                    self.printL(tmp)
                    return tmp
                tmp = tmp.next
                ite += 1


l = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
# l6 = ListNode(6)
l.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
# l5.next = l6
S = Solution()
print(S.middleNode(l))
