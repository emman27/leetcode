from minimum_add_to_make_parentheses_valid import Solution


def test_balanced():
    assert 0 == Solution().minAddToMakeValid("()")


def test_unbalanced_left():
    assert 1 == Solution().minAddToMakeValid("(")
