#
# @lc app=leetcode.cn id=1504 lang=python3
#
# [1504] 统计全 1 子矩形
#

# @lc code=start
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m,n = len(mat), len(mat[0])
        ans = 0
        for top in range(m):
            a = [0] * n
            for bottom in range(top, m):
                h = bottom - top + 1
                last  = -1
                for j in range(n):
                    a[j] += mat[bottom][j]
                    if a[j] != h:
                        last = j
                    else:
                        ans += j-last
        return ans
        
# @lc code=end

