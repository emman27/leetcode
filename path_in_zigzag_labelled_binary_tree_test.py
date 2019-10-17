from path_in_zigzag_labelled_binary_tree import Solution


def test_root():
    assert [1] == Solution().pathInZigZagTree(1)


def test_right():
    assert [1, 2] == Solution().pathInZigZagTree(2)


def test_left():
    assert [1, 3] == Solution().pathInZigZagTree(3)


def test_position_of_final_node():
    assert 1 == Solution()._position_of_final_node(1)
    assert 2 == Solution()._position_of_final_node(2)
    assert 1 == Solution()._position_of_final_node(3)
