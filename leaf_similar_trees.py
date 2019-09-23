from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf_sequence(root1) == self.leaf_sequence(root2)

    def leaf_sequence(self, node: TreeNode) -> List:
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.leaf_sequence(node.left) + self.leaf_sequence(node.right)
