from sort_the_matrix_diagonally import Solution


def test_simple():
    assert [[1, 1, 1], [1, 2, 3]] == Solution().diagonalSort([[2, 3, 1], [1, 1, 1]])
