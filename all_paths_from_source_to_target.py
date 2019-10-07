from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        last_node = len(graph) - 1
        paths: List[List[int]] = []
        potential_paths: List[List[int]] = [[0]]
        while potential_paths:
            path = potential_paths.pop()
            for next_step in graph[path[-1]]:
                if next_step == last_node:
                    paths.append(path + [last_node])
                else:
                    potential_paths.append(path + [next_step])
        return paths
