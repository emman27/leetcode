from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        right_point = None
        for idx, elem in enumerate(preorder):
            if elem > root.val:
                right_point = idx
                break
        root.right = self.bstFromPreorder(preorder[right_point:]) if right_point else None
        root.left = self.bstFromPreorder(preorder[1:right_point]) if len(preorder) > 1 else None
        return root
