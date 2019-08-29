
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
        results = [root.val]
        for child in root.children:
            results.extend(self.preorder(child))
        return results
