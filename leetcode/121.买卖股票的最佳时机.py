#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = prices[0]
        max_profit = 0
        # dp 存储股票最低价钱
        for i in range(1, len(prices)):
            dp = min(dp, prices[i])
            max_profit = max(max_profit, prices[i]-dp)
        return max_profit
# @lc code=end
