#
# @lc app=leetcode.cn id=3330 lang=python3
#
# [3330] 找到初始输入字符串 I
#

# @lc code=start
class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        n = len(word)
        for i in range(1,n):
            if word[i] == word[i-1]:
                ans += 1
            
        return ans
# @lc code=end

