#
# @lc app=leetcode.cn id=1353 lang=python3
#
# [1353] 最多可以参加的会议数目
#

# @lc code=start
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # mx = max(e[1] for e in events)
        # groups = [[]for _ in range(mx+1)]
        # for e in events:
        #     groups[e[0]].append(e[1])
        
        # h = []
        # ans = 0
        # for i,g in enumerate(groups):
        #     while h and h[0]<i:
        #         heappop(h)
        #     for endday in g:
        #         heappush(h,endday)
        #     if h:
        #         ans += 1
        #         heappop(h)
        # return ans
        events.sort(key=lambda x: x[1])
        ans = 0
        mx = events[-1][1]
        fa = list(range(mx+2))
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        for e in events:
            start, end = e
            day = find(start)
            if day <= end:
                ans += 1
                fa[day] = day + 1
        return ans
            
# @lc code=end

