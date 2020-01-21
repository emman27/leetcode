from deepest_leaves_sum import Solution, TreeNode


def test_single_layer():
    assert 1 == Solution().deepestLeavesSum(TreeNode(1))


def test_left_only():
    root = TreeNode(1)
    left = TreeNode(2)
    root.left = left
    assert 2 == Solution().deepestLeavesSum(root)


def test_both():
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    assert 5 == Solution().deepestLeavesSum(root)
