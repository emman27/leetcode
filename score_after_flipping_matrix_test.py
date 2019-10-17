from score_after_flipping_matrix import Solution


def test_already_correct():
    assert 1 == Solution().matrixScore([[1]])
    assert 6 == Solution().matrixScore([[1, 1], [1, 1]])
