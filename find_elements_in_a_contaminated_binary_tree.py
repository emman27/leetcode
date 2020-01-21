# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = {0}
        root.val = 0
        self._recover(root)
        self.root = root

    def _recover(self, root: TreeNode):
        if root is None:
            return
        if root.left is not None:
            root.left.val = 2 * root.val + 1
            self.elements.add(root.left.val)
        if root.right is not None:
            root.right.val = 2 * root.val + 2
            self.elements.add(root.right.val)
        self._recover(root.left)
        self._recover(root.right)

    def find(self, target: int) -> bool:
        return target in self.elements
# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
