from minimum_add_to_make_parentheses_valid import Solution


def test_balanced():
    assert 0 == Solution().minAddToMakeValid("()")


def test_unbalanced_left():
    assert 1 == Solution().minAddToMakeValid("(")


def test_unbalanced_right():
    assert 1 == Solution().minAddToMakeValid(")")


def test_two():
    assert 2 == Solution().minAddToMakeValid(")(")


def test_nested():
    assert 0 == Solution().minAddToMakeValid("((()))")
