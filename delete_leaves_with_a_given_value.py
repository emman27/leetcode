from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        return self._removeLeafNodes(root, target)[0]

    def _removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Tuple[Optional[TreeNode], bool]:
        changed = True
        while changed:
            if not root:
                return None, False
            if root.val == target and root.left is None and root.right is None:
                return None, True
            root.left, left_changed = self._removeLeafNodes(root.left, target)
            root.right, right_changed = self._removeLeafNodes(root.right, target)
            changed = left_changed or right_changed
        return root, changed
