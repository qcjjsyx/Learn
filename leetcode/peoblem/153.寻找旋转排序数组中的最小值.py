#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # red 最小值的左侧
        # blue 最小值的右侧或最小值
        #(left,right)
        left, right = -1, len(nums) - 1
        while left+1<right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                right = mid
            else:
                left = mid
        return nums[right]
        
    
# @lc code=end

