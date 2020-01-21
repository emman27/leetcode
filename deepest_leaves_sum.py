# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    class _Pair:
        def __init__(self, val: int, height: int):
            self.val = val
            self.height = height

    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self._deepestLeavesSum(root, 0).val

    def _deepestLeavesSum(self, root: TreeNode, height: int) -> '_Pair':
        if not (root.left or root.right):
            return self.__class__._Pair(root.val, height)
        elif root.left and root.right:
            left_sum = self._deepestLeavesSum(root.left, height + 1)
            right_sum = self._deepestLeavesSum(root.right, height + 1)
            if left_sum.height > right_sum.height:
                return left_sum
            elif left_sum.height < right_sum.height:
                return right_sum
            return self.__class__._Pair(left_sum.val + right_sum.val, left_sum.height)
        elif root.left:
            return self._deepestLeavesSum(root.left, height + 1)
        elif root.right:
            return self._deepestLeavesSum(root.right, height + 1)
        else:
            raise Exception("not possible")
