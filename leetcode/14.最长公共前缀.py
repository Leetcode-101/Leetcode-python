#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (39.85%)
# Likes:    1637
# Dislikes: 0
# Total Accepted:    534.1K
# Total Submissions: 1.3M
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
# 
# 如果不存在公共前缀，返回空字符串 ""。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：strs = ["flower","flow","flight"]
# 输出："fl"
# 
# 
# 示例 2：
# 
# 
# 输入：strs = ["dog","racecar","car"]
# 输出：""
# 解释：输入不存在公共前缀。
# 
# 
# 
# 提示：
# 
# 
# 0 
# 0 
# strs[i] 仅由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # TODO 优化，可以通过两两匹配去找
        max_length = min([len(s) for s in strs])
        res = ""
        for i in range(max_length):
            _c = strs[0][i]
            for s in strs[1:]:
                if _c != s[i]:
                    return res
            res += _c
        return res                
# @lc code=end
