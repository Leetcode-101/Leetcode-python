#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (47.38%)
# Likes:    465
# Dislikes: 0
# Total Accepted:    45.8K
# Total Submissions: 96.7K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个 m x n 整数矩阵 matrix ，找出其中 最长递增路径 的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你 不能 在 对角线 方向上移动或移动到 边界外（即不允许环绕）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
# 输出：4 
# 解释：最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2：
# 
# 
# 输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
# 输出：4 
# 解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
# 示例 3：
# 
# 
# 输入：matrix = [[1]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        max_length = 0
        m = len(matrix)
        n = len(matrix[0])

        # @lru_cache(None)
        def get_dfs(_i, _j):
            if cache.get(f"#{_i}##{_j}"):
                return cache.get(f"#{_i}##{_j}")
            _best = 1
            for offset_i, offset_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                cur_i = _i + offset_i
                cur_j = _j + offset_j
                if 0 <= cur_i < m and 0 <= cur_j < n and matrix[_i][_j] < matrix[cur_i][cur_j]:
                    _best = max(_best, get_dfs(cur_i, cur_j) + 1)
            cache[f"#{_i}##{_j}"] = _best
            return _best

        for i in range(m):
            for j in range(n):
                max_length = max(max_length, get_dfs(i, j))
        return max_length
# @lc code=end
