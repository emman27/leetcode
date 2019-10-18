from recover_a_tree_from_preorder_traversal import Solution, TreeNode


def test_trivial():
    assert TreeNode(1) == Solution().recoverFromPreorder("1")
