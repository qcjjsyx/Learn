#
# @lc app=leetcode.cn id=3304 lang=python3
#
# [3304] 找出第 K 个字符 I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s = [0]
        while len(s) < k:
            for i in range(len(s)):
                s.append((s[i] + 1) % 26)
        return alphabet[s[k - 1]]        
# @lc code=end

