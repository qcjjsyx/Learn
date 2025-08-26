#
# @lc app=leetcode.cn id=3440 lang=python3
#
# [3440] 重新安排会议得到最多空余时间 II
#

# @lc code=start
class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        def get(i):
           if i==0:
               return startTime[0]
           if i==n:
               return eventTime- endTime[-1]
           return startTime[i] - endTime[i-1]

        a,b,c = 0,-1,-1
        for i in range(1,n+1):
            if get(i)>get(a):
                a,b,c = i,a,b
            elif get(i)>get(b) or b<0:
                b,c = i,b
            elif get(i)>get(c) or c<0:
                c = i
        ans = 0
        for i,(s,e) in enumerate(zip(startTime, endTime)):
            spendTime = e-s
            if i!=a and i+1!=a and get(a)>=spendTime or i!=b and i+1!=b and get(b)>=spendTime or get(c)>=spendTime:
                ans = max(ans, spendTime+get(i)+get(i+1))
            else:
                ans = max(ans, get(i)+get(i+1))
        return ans

# @lc code=end

