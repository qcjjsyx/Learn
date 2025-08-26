#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        path = []
        def backtrack(index,path):
            if index == len(s):
                ans.append(''.join(path))
                return
            if s[index].isalpha():
                path.append(s[index].lower())
                backtrack(index + 1, path)
                path.pop()
                path.append(s[index].upper())
                backtrack(index + 1, path)
                path.pop()
            else:
                path.append(s[index])
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, path)
        return ans
# @lc code=end

