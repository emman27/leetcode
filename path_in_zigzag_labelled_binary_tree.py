from math import ceil, floor, log2
from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        position = self._position_of_final_node(label)
        height = self._height(label)
        path = []
        while height != 0:
            path.append(self._label_at(height, position))
            height -= 1
            position = ceil(position/2)
        return path[::-1]

    def _total_at_height(self, height: int) -> int:
        return 2 ** (height - 1)

    def _is_forward(self, height: int) -> bool:
        return height % 2 == 1

    def _total_nodes_up_to_height(self, height):
        return (1 * (2**(height) - 1))

    def _position_of_final_node(self, label: int) -> int:
        height = self._height(label)
        return (label - self._total_nodes_up_to_height(height-1) if
                self._is_forward(height) else
                self._total_nodes_up_to_height(height) - label + 1)

    def _height(self, label: int) -> int:
        return floor(log2(label)) + 1

    def _label_at(self, height: int, position: int) -> int:
        return (self._total_nodes_up_to_height(height-1) + position if
                self._is_forward(height) else
                self._total_nodes_up_to_height(height)-position + 1)
