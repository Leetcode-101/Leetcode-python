#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#
# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (37.18%)
# Likes:    5509
# Dislikes: 0
# Total Accepted:    1M
# Total Submissions: 2.7M
# Testcase Example:  '"abcabcbb"'
#
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 
# 
# 示例 2:
# 
# 
# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 
# 
# 示例 3:
# 
# 
# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
# 
# 
# 示例 4:
# 
# 
# 输入: s = ""
# 输出: 0
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# s 由英文字母、数字、符号和空格组成
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 窗口向右滑动，不满足条件时跳出
        L, R = 0, -1
        length = 0
        word_set = set()
        while R < len(s):
            while R < len(s):
                R += 1
                if R == len(s):
                    break
                if s[R] not in word_set:
                    word_set.add(s[R])
                    length = max(len(word_set), length)
                else:
                    break
            # 不可使用len(s)-1;R内层break和外层break有区别
            if R == len(s):
                break
            while L < R:
                if s[L] != s[R]:
                    word_set.remove(s[L])
                    L += 1
                else:
                    L += 1
                    break
        return length
# @lc code=end
