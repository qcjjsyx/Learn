#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
import collections
from typing import List
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        cnt = collections.Counter(nums)
        for key in cnt:
            if key+1 in cnt:
                ans = max(ans, cnt[key] + cnt[key+1])
        return ans
# @lc code=end

