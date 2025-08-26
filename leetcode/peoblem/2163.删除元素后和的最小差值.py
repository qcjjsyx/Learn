#
# @lc app=leetcode.cn id=2163 lang=python3
#
# [2163] 删除元素后和的最小差值
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        m = n//3
        min_h = nums[-m:]
        heapify(min_h)
        suf_max = [0]*(n-m+1)
        suf_max[-1] = sum(min_h)
        for i in range(n-m-1,m-1,-1):
            suf_max[i] = suf_max[i+1]+nums[i]-heappushpop(min_h, nums[i])
            
        max_h = [-x for x in nums[:m]]
        heapify(max_h)
        pre_min = -sum(max_h)
        ans = pre_min - suf_max[m]
        for i in range(m,n-m):
            pre_min += nums[i] + heappushpop(max_h,-nums[i])
            ans = min(ans, pre_min - suf_max[i+1])
        return ans
# @lc code=end

