from matrix_block_sum import Solution


def test_cache_generation():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    cache = Solution()._generate_cache(mat)
    assert [[1, 3, 6], [5, 12, 21], [12, 27, 45]] == cache


def test_all():
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert [[12, 21, 16], [27, 45, 33], [24, 39, 28]] == Solution().matrixBlockSum(mat, 1)
