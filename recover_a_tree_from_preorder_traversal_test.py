from recover_a_tree_from_preorder_traversal import Solution, TreeNode


def test_trivial():
    assert TreeNode(1) == Solution().recoverFromPreorder("1")


def test_single_layer():
    solution = TreeNode(1)
    solution.left = TreeNode(2)
    solution.right = TreeNode(3)
    assert solution == Solution().recoverFromPreorder("1-2-3")

    half = TreeNode(1)
    half.left = TreeNode(2)
    assert half == Solution().recoverFromPreorder("1-2")


def test_multilayer():
    expected = TreeNode(1)
    expected.left = TreeNode(2)
    expected.left.left = TreeNode(3)
    expected.left.right = TreeNode(4)
    expected.right = TreeNode(5)
    expected.right.left = TreeNode(6)
    expected.right.right = TreeNode(7)
    assert expected == Solution().recoverFromPreorder("1-2--3--4-5--6--7")


def test_unbalanced():
    expected = TreeNode(1)
    expected.left = TreeNode(2)
    expected.left.left = TreeNode(3)
    expected.left.left.left = TreeNode(4)
    expected.right = TreeNode(5)
    expected.right.left = TreeNode(6)
    expected.right.left.left = TreeNode(7)
    assert expected == Solution().recoverFromPreorder("1-2--3---4-5--6---7")
