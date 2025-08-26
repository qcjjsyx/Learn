#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # right 表示顶峰的左侧，即right+1 可能是顶峰
        # left 可能是顶峰，
        n = len(nums)
        if n == 1:
            return 0
        left,right = 0,n-2
        while left <= right:
            mid = (left+right)//2
            if nums[mid] >nums[mid+1]:
                right = mid-1
            else:
                left = mid+1
        return left
# @lc code=end

