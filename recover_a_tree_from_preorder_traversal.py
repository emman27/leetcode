# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        return TreeNode(int(S[0]))
