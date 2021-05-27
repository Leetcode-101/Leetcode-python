#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (41.44%)
# Likes:    1170
# Dislikes: 0
# Total Accepted:    139.9K
# Total Submissions: 337.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
#
# 注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # TODO 考虑优化
        # 保存t不在子穿中的字符个数
        items_t = {}
        res = ""
        min_length = len(s) + 1
        for i in t:
            items_t[i] = items_t.get(i, 0) + 1

        def check():
            for _, v in items_t.items():
                if v > 0:
                    return False
            return True
        # 滑动窗口
        L, R = 0, -1
        while R < len(s):
            while R < len(s):
                R += 1
                if R == len(s):
                    break
                if s[R] in items_t:
                    items_t[s[R]] = items_t[s[R]] - 1

                if check():
                    if R - L + 1 < min_length:
                        min_length = R - L + 1
                        res = s[L:R+1]
                    break

            if R == len(s):
                break

            while L < R:
                if s[L] in items_t:
                    items_t[s[L]] = items_t[s[L]] + 1
                L += 1
                if not check():
                    break
                # 找最小，R到底，L缩短的时候，会更新最小值
                if R - L + 1 < min_length:
                    min_length = R - L + 1
                    res = s[L:R+1]

        return res
# @lc code=end
