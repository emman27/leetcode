# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        length = self._len(head)
        middle_index = int(length/2)
        for i in range(middle_index):
            head = head.next
        return head

    def _len(self, head: ListNode) -> int:
        def helper(head, current_length):
            if head is None:
                return 0
            return 1 + helper(head.next, current_length)
        return helper(head, 0)
