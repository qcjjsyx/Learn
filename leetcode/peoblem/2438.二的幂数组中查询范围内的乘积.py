#
# @lc app=leetcode.cn id=2438 lang=python3
#
# [2438] 二的幂数组中查询范围内的乘积
#

# @lc code=start
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 1_000_000_007
        powers = []
        i = 0
        while (1 << i) <= n:
            if n & (1 << i):
                powers.append(1 << i)
            i += 1
        prefix = [powers[0]]
        for i in range(1, len(powers)):
            prefix.append((prefix[-1] * powers[i]) % MOD)
        ans = []
        for query in queries:
            left, right = query[0], query[1]
            if left == 0:
                ans.append(prefix[right])
            else:
                ans.append((prefix[right] * pow(prefix[left - 1], MOD - 2, MOD)) % MOD)
        return ans
# @lc code=end

