#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        ## solution 1: 前后缀最大值
        ## 时间复杂度 O(n), 空间复杂度 O(n)
        # n = len(height)
        # if n<3:
        #     return 0
        # pre_max = [height[0]] * n
        # suf_max = [height[-1]] * n
        # for i in range(1,n):
        #     pre_max[i] = max(pre_max[i-1], height[i])
        # for i in range(n-2, -1, -1):
        #     suf_max[i] = max(suf_max[i+1], height[i])
            
        # ans = 0
        # for i in range(1,n-1):
        #     ans += min(pre_max[i], suf_max[i]) - height[i]
        # return ans
        
        ## solution 2: 双指针
        ## 时间复杂度 O(n), 空间复杂度 O(1)
        n = len(height)
        l,r = 0, n-1
        pre_max, suf_max = height[l], height[r]
        ans = 0
        while l<=r:
            pre_max = max(pre_max, height[l])
            suf_max = max(suf_max, height[r])
            if pre_max < suf_max:
                ans += pre_max - height[l]
                l += 1
            else:
                ans += suf_max - height[r]
                r -= 1
        return ans
# @lc code=end

