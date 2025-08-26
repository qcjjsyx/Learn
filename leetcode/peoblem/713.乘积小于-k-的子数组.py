#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans,n = 0,len(nums)
        left,right,product = 0,0,1
        for right in range(n):
            product *= nums[right]
            while left <= right and product >= k:
                product //= nums[left]
                left += 1
            ans += right - left + 1
        return ans
# @lc code=end

