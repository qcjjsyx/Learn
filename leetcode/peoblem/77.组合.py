#
# @lc app=leetcode.cn id=77 lang=python3
#
# [77] 组合
#

# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        path = []
        def backtrack(i):
            if len(path) == k:
                ans.append(path.copy())
                return
            if i<k-len(path):
                return
            
            for j in range(i,0,-1):
                path.append(j)
                backtrack(j-1)
                path.pop()
        backtrack(n)
        return ans
# @lc code=end

