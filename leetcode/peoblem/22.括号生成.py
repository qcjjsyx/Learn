#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = 2 * n
        ans = []
        path = []
        def dfs(i,open):
            if len(path) == m:
                ans.append(''.join(path))
                return
            if open < n:
                path.append('(')
                dfs(i + 1, open + 1)
                path.pop()
            if i - open < open:
                path.append(')')
                dfs(i + 1, open)
                path.pop()
        dfs(0, 0)
        return ans
                
# @lc code=end

