#
# @lc app=leetcode.cn id=3439 lang=python3
#
# [3439] 重新安排会议得到最多空余时间 I
#

# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        ans = 0
        n = len(startTime)
        f = [0]*(n+1)
        f[0] = startTime[0]-0
        for i in range(1,n):
            f[i] = startTime[i]-endTime[i-1]
        f[n] = eventTime-endTime[n-1]
        # print(f)
        temp = 0
        for i in range(n+1):
            temp += f[i]
            if i<k:
                continue
            ans = max(ans, temp)
            temp -= f[i-k]
        return ans
# @lc code=end

