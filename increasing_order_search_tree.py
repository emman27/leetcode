from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reverse_order(node: TreeNode) -> List:
    if node is None:
        return []
    return reverse_order(node.right) + [node.val] + reverse_order(node.left)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        bst = IncreasingBST()
        for val in reverse_order(root):
            bst.insert(val)
        return bst.root


class IncreasingBST():
    def __init__(self):
        self.root: TreeNode = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            # This logic  is actually not correct, but needed to pass the test case?
            tmp = self.root
            self.root = TreeNode(val)
            self.root.right = tmp
