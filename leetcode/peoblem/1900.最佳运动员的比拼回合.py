#
# @lc app=leetcode.cn id=1900 lang=python3
#
# [1900] 最佳运动员的比拼回合
#

# @lc code=start
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @cache
        def dfs(n,first,second):
            if first+second == n+1:
                return 1,1
            if first+second > n+1:
                first,second = n+1-second, n+1-first
                
            m = (n+1)//2
            min_mid = 0 if second <= m else second - n//2-1
            max_mid = second-first if second <= m else m-first
            earliest = float('inf')
            latest = 0
            for left in range(first):
                for mid in range(min_mid, max_mid):
                    e,l = dfs(m,left+1,left+mid+2)
                    earliest = min(earliest, e)
                    latest = max(latest, l)
            return earliest + 1, latest + 1
        return list(dfs(n, firstPlayer, secondPlayer))
# @lc code=end

