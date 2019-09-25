from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maximum_index, maximum = max(enumerate(nums), key=lambda item: item[1])
        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(nums[:maximum_index])
        root.right = self.constructMaximumBinaryTree(nums[maximum_index+1:])
        return root
