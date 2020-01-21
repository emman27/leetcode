from all_elements_in_two_binary_search_trees import Solution, TreeNode


def test_single_tree():
    root1 = TreeNode(1)
    root1.left = TreeNode(0)
    root1.right = TreeNode(2)
    root2 = None
    assert [0, 1, 2] == Solution().getAllElements(root1, root2)


def test_two_trees():
    root1 = TreeNode(2)
    root1.left = TreeNode(0)
    root1.right = TreeNode(4)
    root2 = TreeNode(3)
    root2.left = TreeNode(1)
    root2.right = TreeNode(5)
    assert [0, 1, 2, 3, 4, 5] == Solution().getAllElements(root1, root2)
