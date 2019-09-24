from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        return self._bstToGst(root, self._sort(root))

    def _bstToGst(self, root: TreeNode, sorted_values: List[int]) -> TreeNode:
        if root is None:
            return None
        root.left = self._bstToGst(root.left, sorted_values)
        root.right = self._bstToGst(root.right, sorted_values)
        root.val = sum(sorted_values[sorted_values.index(root.val):])
        return root

    def _sort(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self._sort(root.left) + [root.val] + self._sort(root.right)
