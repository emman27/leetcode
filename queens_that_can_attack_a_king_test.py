from queens_that_can_attack_a_king import Solution

sol = Solution()


def test_right():
    assert [[0, 1]] == sol.queensAttacktheKing([[0, 1]], [0, 0])


def test_down():
    assert [[1, 0]] == sol.queensAttacktheKing([[1, 0]], [0, 0])


def test_left():
    assert [[0, 0]] == sol.queensAttacktheKing([[0, 0]], [0, 1])


def test_southeast():
    assert [[1, 1]] == sol.queensAttacktheKing([[1, 1]], [0, 0])
    assert [[6, 7]] == sol.queensAttacktheKing([[6, 7]], [5, 6])
