# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def removeNthFromEnd(self, head, n):
        points_to_head = ListNode()
        points_to_head.next = head

        leader = follower = head
        prev = points_to_head

        count = 0

        # Creating a window of size n - between leader and follower
        while count < n and leader:
            leader = leader.next
            count += 1

        # Traversing until leader reaches null - such that when we exit the loop
        # Follower points to N th node from last
        while leader:
            leader = leader.next
            prev = follower
            follower = follower.next

        # Deleting follower node
        prev.next = follower.next

        # Should use the pointer we have to head
        # To handle single element cases
        return points_to_head.next


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
print(S.removeNthFromEnd(l, 4))
