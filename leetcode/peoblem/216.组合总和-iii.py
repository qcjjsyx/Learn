#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#

# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(i,t):
            if len(path) == k and t == 0:
                ans.append(path.copy())
                return
            d = k - len(path)
            if i<d or t<0:
                return
            if t>(2*i - d + 1) * d // 2:
                return

            for j in range(i,0,-1):
                path.append(j)
                t -= j
                dfs(j-1,t)
                path.pop()
                t += j
        dfs(9,n)
        return ans
        
# @lc code=end

