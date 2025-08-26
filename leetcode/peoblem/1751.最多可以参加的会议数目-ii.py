#
# @lc app=leetcode.cn id=1751 lang=python3
#
# [1751] 最多可以参加的会议数目 II
#

# @lc code=start
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        if k==1:
            return max(e[2] for e in events)
        events.sort(key=lambda x: x[1])
        dp  = [[0]*(k+1) for _ in range(len(events)+1)]
        for i,(st,et,val) in enumerate(events):
             p = bisect_left(events,st,hi=i,key=lambda x:x[1])
             for j in range(1,k+1):
                 dp[i+1][j] = max(dp[i][j],dp[p][j-1]+val)
        return dp[-1][-1]
        
# @lc code=end

