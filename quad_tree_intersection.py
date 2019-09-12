from typing import List

# Definition for a QuadTree node.


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: Node, quadTree2: Node) -> Node:
        if quadTree1.isLeaf:
            return quadTree1 if quadTree1.val else quadTree2
        elif quadTree2.isLeaf:
            return quadTree2 if quadTree2.val else quadTree1
        top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
        if self._all_are_leaves([top_left, top_right, bottom_left, bottom_right]) and self._all_same_value([top_left, top_right, bottom_left, bottom_right]):
            return Node(top_left.val, True, None, None, None, None)
        return Node(None, False, top_left, top_right, bottom_left, bottom_right)

    def _all_are_leaves(self, nodes: List[Node]) -> bool:
        for node in nodes:
            if not node.isLeaf:
                return False
        return True

    def _all_same_value(self, nodes: List[Node]) -> bool:
        if not nodes:
            return True
        first_value = nodes[0].val
        for node in nodes:
            if node.val != first_value:
                return False
        return True
