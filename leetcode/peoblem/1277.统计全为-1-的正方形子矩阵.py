#
# @lc app=leetcode.cn id=1277 lang=python3
#
# [1277] 统计全为 1 的正方形子矩阵
#

# @lc code=start
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        m,n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 0
        ans = sum(dp[i][j] for i in range(m) for j in range(n))
        return ans
# @lc code=end

