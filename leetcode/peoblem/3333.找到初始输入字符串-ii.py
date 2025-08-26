#
# @lc app=leetcode.cn id=3333 lang=python3
#
# [3333] 找到初始输入字符串 II
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        ans = 1
        n = len(word)
        if n<k:
            return 0
        MOD = 1_000_000_007
        cnts = []
        cnt = 0
        for i in range(n):
            cnt += 1
            if i==n-1 or word[i]!=word[i+1]:
                if cnt>1:
                    if k>0:
                        cnts.append(cnt-1)
                    ans = ans*cnt% MOD
                k -= 1
                cnt = 0
        if k<=0:
            return ans
        
        f = [[0]*k for _ in range(len(cnts)+1)]
        f[0] = [1]*k
        for i, c in enumerate(cnts):
            s = list(accumulate(f[i],initial=0))
            for j in range(k):
                f[i+1][j] = (s[j+1]-s[max(0,j-c)])%MOD
        
        return (ans-f[-1][-1])%MOD
# @lc code=end

