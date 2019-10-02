from all_possible_full_binary_trees import Solution, TreeNode


def test_one():
    assert Solution().allPossibleFBT(1) == [TreeNode(0)]


def test_two():
    assert Solution().allPossibleFBT(2) == []


def test_three():
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    assert Solution().allPossibleFBT(3) == [root]


def test_seven():
    assert len(Solution().allPossibleFBT(7)) == 5
