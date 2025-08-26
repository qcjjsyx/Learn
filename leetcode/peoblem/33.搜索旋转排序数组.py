#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i):
            if nums[i] > nums[-1]:
                return target > nums[-1] and target <= nums[i]
            else:
                return target > nums[-1] or target <= nums[i]
        left, right = -1, len(nums) 
        while left + 1 < right:
            mid = (left + right) // 2
            if is_blue(mid):
                right = mid
            else:
                left = mid
        if right==len(nums) or nums[right] != target:
            return -1
        return right
# @lc code=end

