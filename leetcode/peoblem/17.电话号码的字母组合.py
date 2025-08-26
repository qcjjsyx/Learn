#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
MAPPING = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        def backtrack(i,path):
            if i==len(digits):
                ans.append(path)
                return 
            for c in MAPPING[int(digits[i])]:
                backtrack(i+1,path+c)
        backtrack(0,"")
        return ans
# @lc code=end

