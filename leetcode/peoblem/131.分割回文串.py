#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#

# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            i,j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        ans = []
        path = []
        n = len(s)
        def backtrack(i: int):
            if i==n:
                ans.append(path.copy())
                return 
            for j in range(i,n):
                temp = s[i:j+1]
                if is_palindrome(temp):
                    path.append(temp)
                    backtrack(j+1)
                    path.pop()
        backtrack(0)
        return ans
# @lc code=end

