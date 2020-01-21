from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        return self._merge_sort(self._flatten(root1), self._flatten(root2))

    def _flatten(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self._flatten(root.left) + [root.val] + self._flatten(root.right)

    def _merge_sort(self, list1: List[int], list2: List[int]):
        result = []
        while list1 and list2:
            left = list1[0]
            right = list2[0]
            if left < right:
                result.append(list1.pop(0))
            elif left > right:
                result.append(list2.pop(0))
            else:
                result.append(list1.pop(0))
                result.append(list2.pop(0))
        result.extend(list1)
        result.extend(list2)
        return result
