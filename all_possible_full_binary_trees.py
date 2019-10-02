from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N == 1:
            return [TreeNode(0)]
        elif N % 2 == 0:
            return []
        trees = []
        for i in range(1, N, 2):
            for left_tree in self.allPossibleFBT(i):
                for right_tree in self.allPossibleFBT(N-i-1):
                    root = TreeNode(0)
                    root.left = left_tree
                    root.right = right_tree
                    trees.append(root)
        return trees
