# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return (self._sum_of_grandchildren(root) if root.val % 2 == 0 else 0) + self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)

    def _sum_of_grandchildren(self, root: TreeNode) -> int:
        if root is None:
            return 0
        total = 0
        left = root.left
        right = root.right
        if left:
            total += left.left.val if left.left else 0
            total += left.right.val if left.right else 0
        if right:
            total += right.right.val if right.right else 0
            total += right.left.val if right.left else 0
        return total
