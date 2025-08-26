#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1]]
        for i in range(2,numRows + 1):
            row = [1] * i
            for j in range(1,i-1):
                row[j] = ans[-1][j-1]+ans[-1][j]
            ans.append(row)
        return ans

# @lc code=end

