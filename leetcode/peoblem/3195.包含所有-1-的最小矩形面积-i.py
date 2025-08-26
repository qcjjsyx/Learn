#
# @lc app=leetcode.cn id=3195 lang=python3
#
# [3195] 包含所有 1 的最小矩形面积 I
#

# @lc code=start
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        left,right,top,bottom = 0,n-1,0,m-1
        for j in range(n):
            if any(grid[i][j] == 1 for i in range(m)):
                left = j
                break
        for j in range(n-1,-1,-1):
            if any(grid[i][j] == 1 for i in range(m)):
                right = j
                break
        for i in range(m):
            if any(grid[i][j] == 1 for j in range(n)):
                top = i
                break
        for i in range(m-1,-1,-1):
            if any(grid[i][j] == 1 for j in range(n)):
                bottom = i
                break
        return (right-left+1) * (bottom-top+1) if left <= right and top <= bottom else 0
# @lc code=end

