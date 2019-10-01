from typing import Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.levels: Dict[int, int] = {}
        self.recurse_binary_tree(root, 1)
        maximum_sum = max(self.levels.values())
        return min(filter(lambda key: self.levels[key] == maximum_sum, self.levels.keys()))

    def recurse_binary_tree(self, root: TreeNode, current_level: int):
        if root is None:
            return
        self.levels[current_level] = self.levels.get(current_level, 0) + root.val
        self.recurse_binary_tree(root.left, current_level + 1)
        self.recurse_binary_tree(root.right, current_level + 1)
