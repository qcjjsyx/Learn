#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []
        def dfs(i,t):
            if t==0:
                ans.append(path.copy())
                return
            if i < 0 or t < candidates[0]:
                return
            
            for j in range(i,-1,-1):
                path.append(candidates[j])
                dfs(j,t-candidates[j])
                path.pop()
           
            
        dfs(len(candidates)-1, target)
        return ans
# @lc code=end

