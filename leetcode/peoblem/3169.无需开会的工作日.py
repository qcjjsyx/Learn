#
# @lc app=leetcode.cn id=3169 lang=python3
#
# [3169] 无需开会的工作日
#

# @lc code=start
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        ans = days
        start, end = 1,0
        for s,e in meetings:
            if s>end:
                ans -= (end-start+1)
                start = s
            end = max(end, e)
        ans -= (end-start+1)
        return ans
# @lc code=end

