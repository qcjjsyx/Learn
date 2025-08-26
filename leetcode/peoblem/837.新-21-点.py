#
# @lc app=leetcode.cn id=837 lang=python3
#
# [837] 新 21 点
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0.0]*(k+maxPts)
        for i in range(k, min(n+1, k+maxPts)):
            dp[i] = 1.0
        suf_sum = sum(dp[k:k+maxPts])
        for i in range(k-1, -1, -1):
            dp[i] = suf_sum / maxPts
            suf_sum += dp[i] - (dp[i + maxPts] if i + maxPts < len(dp) else 0)
        return dp[0]
# @lc code=end

