from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        not_in_arr_2 = sorted(filter(lambda x: x not in arr2, arr1))
        arr2_expanded = [[elem] * arr1.count(elem) for elem in arr2]
        results = []
        for elem in arr2_expanded:
            results.extend(elem)
        results.extend(not_in_arr_2)
        return results
