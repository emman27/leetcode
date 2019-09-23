from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return []
        num_cols = len(A)
        num_rows = len(A[0])
        base_row = [0] * num_cols
        transposed: List[List[int]] = []
        for i in range(num_rows):
            transposed.append(base_row.copy())
        for (row_num, row) in enumerate(A):
            for (col_num, val) in enumerate(row):
                transposed[col_num][row_num] = val
        return transposed
