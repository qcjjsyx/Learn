#
# @lc app=leetcode.cn id=1233 lang=python3
#
# [1233] 删除子文件夹
#

# @lc code=start
class Trie:
    def __init__(self):
        self.children = dict()
        self.ref = -1
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Trie()
        for i,path in enumerate(folder):
           path = path.split('/')
           cur = root
           for p in path:
               if p not in cur.children:
                   cur.children[p] = Trie()
               cur = cur.children[p]
           cur.ref = i
           
        ans = []
        def dfs(cur):
            if cur.ref != -1:
                ans.append(folder[cur.ref])
                return 
            for child in cur.children.values():
                dfs(child)
        dfs(root)
        return ans
            
        # folder.sort()
        # ans = [folder[0]]
        # for i in range(1, len(folder)):
        #     latest = ans[-1]
        #     if not folder[i].startswith(latest + '/'):
        #         ans.append(folder[i])
        # return ans
# @lc code=end

