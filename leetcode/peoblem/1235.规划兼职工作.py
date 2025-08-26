#
# @lc app=leetcode.cn id=1235 lang=python3
#
# [1235] 规划兼职工作
#

# @lc code=start
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        # print(jobs)
        dp = [0] * (len(jobs) + 1)
        for i, (et, st, val) in enumerate(jobs):
            j = bisect_left(jobs, (st + 1,), hi=i)
            dp[i + 1] = max(dp[i], dp[j] + val)
        print(dp)
        return dp[-1]
# @lc code=end

