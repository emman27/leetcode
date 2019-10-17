from score_after_flipping_matrix import Solution


def test_already_correct():
    assert 1 == Solution().matrixScore([[1]])
    assert 6 == Solution().matrixScore([[1, 1], [1, 1]])


def test_flips_rows_that_start_with_zero():
    assert 1 == Solution().matrixScore([[0]])
    assert 6 == Solution().matrixScore([[0, 0], [0, 0]])


def test_flips_columns():
    assert 6 == Solution().matrixScore([
        [1, 0],
        [1, 0]
    ])
