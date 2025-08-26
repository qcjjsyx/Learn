#
# @lc app=leetcode.cn id=3363 lang=python3
#
# [3363] 最多可收集的水果数目
#

# @lc code=start
class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        def dp(fruits):
            n = len(fruits)
            f = [[0]*(n+1) for _ in range(n-1)]
            f[0][n - 1] = fruits[0][-1]
            for i in range(1,n-1):
                for j in range(max(n-1-i,i+1),n):
                    f[i][j] = max(f[i-1][j-1],f[i-1][j],f[i-1][j+1])+fruits[i][j]
            return f[-1][n-1]
        ans = sum(row[i] for i, row in enumerate(fruits))
        return ans + dp(fruits)+dp(list(zip(*fruits)))  # 计算正序和逆序的最大值
               
