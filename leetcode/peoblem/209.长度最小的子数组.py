#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        ans = n+1
        l, r,sum = 0, 0,0
        for r in range(n):
            sum += nums[r]
            while sum >= target :
                ans = min(ans, r - l + 1)
                sum -= nums[l]
                l += 1
            
        return ans if ans != n+1 else 0
# @lc code=end

