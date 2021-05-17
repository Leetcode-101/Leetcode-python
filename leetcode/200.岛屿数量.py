# @before-stub-for-debug-begin
from python3problem200 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=200 lang=python3
#
# [200] 岛屿数量
#
# https://leetcode-cn.com/problems/number-of-islands/description/
#
# algorithms
# Medium (53.80%)
# Likes:    1151
# Dislikes: 0
# Total Accepted:    251.2K
# Total Submissions: 466.9K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 
# 此外，你可以假设该网格的四条边均被水包围。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","1","1","0"],
# ⁠ ["1","1","0","1","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","0","0","0"]
# ]
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：grid = [
# ⁠ ["1","1","0","0","0"],
# ⁠ ["1","1","0","0","0"],
# ⁠ ["0","0","1","0","0"],
# ⁠ ["0","0","0","1","1"]
# ]
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# m == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 的值为 '0' 或 '1'
# 
# 
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                area = 0
                stack = [(i, j)]
                while stack:
                    _i, _j = stack.pop()
                    if _i < 0 or _j < 0 or _i == m or _j == n or grid[_i][_j] == '0':
                        continue
                    if grid[_i][_j]:
                        area += 1
                    grid[_i][_j] = '0'
                    for offset_i, offset_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        stack.append((_i+offset_i, _j+offset_j))
                if area:
                    num_islands += 1

        return num_islands
# @lc code=end
