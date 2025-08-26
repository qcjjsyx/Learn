#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        n = len(nums)
        def backtrack(i):
            if i==n:
                ans.append(path.copy())
                return 
            # 不选当前元素
            backtrack(i+1)
            # 选当前元素
            path.append(nums[i])
            backtrack(i+1)
            path.pop()
        backtrack(0)
        return ans
# @lc code=end

