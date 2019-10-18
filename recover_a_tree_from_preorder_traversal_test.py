from recover_a_tree_from_preorder_traversal import Solution, TreeNode


def test_trivial():
    assert TreeNode(1) == Solution().recoverFromPreorder("1")


def test_single_layer():
    solution = TreeNode(1)
    solution.left = TreeNode(2)
    solution.right = TreeNode(3)
    assert solution == Solution().recoverFromPreorder("1-2-3")
