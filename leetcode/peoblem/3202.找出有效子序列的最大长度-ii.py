#
# @lc app=leetcode.cn id=3202 lang=python3
#
# [3202] 找出有效子序列的最大长度 II
#

# @lc code=start
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        ans = 0
        for m in range(k):
            f = [0]*k
            for num in nums:
                x = num % k
                f[x] = f[m-x]+1
            ans = max(ans, max(f))
        
        return ans
# @lc code=end

