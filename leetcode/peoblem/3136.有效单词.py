#
# @lc app=leetcode.cn id=3136 lang=python3
#
# [3136] 有效单词
#

# @lc code=start
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) <= 2:
            return False
        flag_yuan, flag_fu = False, False
        for c in word:
            if c.isalpha():
                if c.lower() in 'aeiou':
                    flag_yuan = True
                else:
                    flag_fu = True
            elif not c.isdigit():
                return False
        return flag_yuan and flag_fu
                
# @lc code=end

