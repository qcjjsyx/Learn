#
# @lc app=leetcode.cn id=301 lang=python3
#
# [301] 删除无效的括号
#

# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        lremove, rlemove = 0, 0
        for c in s:
            if c == '(':
                lremove += 1
            elif c == ')':
                if lremove > 0:
                    lremove -= 1
                else:
                    rlemove += 1
        ans = []
        path = []
        def dfs(i,removedl, removedr, open):
            if i == len(s):
                if removedl == lremove and removedr == rlemove:
                    ans.append(''.join(path))
                return

            ## 尝试删除
            if s[i] == '(' and removedl < lremove:
                dfs(i+1, removedl + 1, removedr, open)
            elif s[i] == ')' and removedr < rlemove:
                dfs(i+1, removedl, removedr + 1, open)
                
            path.append(s[i])
            if s[i] == '(':
                dfs(i+1, removedl, removedr, open + 1)
            elif s[i] == ')':
                if open > 0:
                    dfs(i+1, removedl, removedr, open - 1)
            else:
                dfs(i+1, removedl, removedr, open)
            path.pop()
        dfs(0, 0, 0, 0)
        return ans
# @lc code=end

