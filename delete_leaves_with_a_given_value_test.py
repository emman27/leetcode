from delete_leaves_with_a_given_value import Solution, TreeNode


def test_no_removals():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution().removeLeafNodes(root, 4)
    assert 1 == sol.val
    assert sol.left
    assert sol.right


def test_root_match():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution().removeLeafNodes(root, 1)
    assert 1 == sol.val
    assert sol.left
    assert sol.right


def test_single_leaf_removal():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    sol = Solution().removeLeafNodes(root, 3)
    assert 1 == sol.val
    assert sol.left
    assert sol.right is None


def test_recursive_removal():
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    sol = Solution().removeLeafNodes(root, 1)
    assert sol is None
