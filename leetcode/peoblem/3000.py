#
# @lc app=leetcode.cn id=3000 lang=python3
#
# [3000] 对角线最长的矩形的面积
#

# @lc code=start
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans = 0
        length = 0
        for dimension in dimensions:
            l,w = dimension[0],dimension[1]
            if l*l+w*w > length:
                length = l*l+w*w
                ans = l*w
            elif l*l+w*w == length:
                ans = max(ans,l*w)
        return ans
# @lc code=end