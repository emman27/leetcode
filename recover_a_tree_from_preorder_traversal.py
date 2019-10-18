# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        if bool(self) != bool(other):
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        nodes = [int(val) for val in S.split('-') if val]
        root = TreeNode(nodes[0])
        if len(nodes) > 1:
            root.left = TreeNode(nodes[1])
            root.right = TreeNode(nodes[2])
        return root
