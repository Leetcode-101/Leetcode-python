#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (51.24%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    79K
# Total Submissions: 154K
# Testcase Example:  '16'
#
# 给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x
#
#
#
# 示例 1：
#
#
# 输入：n = 16
# 输出：true
#
#
# 示例 2：
#
#
# 输入：n = 5
# 输出：false
#
#
# 示例 3：
#
#
# 输入：n = 1
# 输出：true
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#
#
# 进阶：
#
#
# 你能不使用循环或者递归来完成本题吗？
#
#
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            t = math.sqrt(n)
            if t * t != n:
                return False

            def low_bit(m):
                return m & (-m)
            # 返回x的二进制最小的1对应的值，2的幂二进制表示为100000...
            # 这个1则代表x的值
            # 正数的补码等于原码  负数的补码 等于 原码取反+1

            return n == low_bit(n)
# @lc code=end
