#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # ans = []
        # def dfs(node, depth):
        #     if not node:
        #         return
        #     if depth == len(ans):
        #         ans.append(node.val)
        #     dfs(node.right, depth + 1)
        #     dfs(node.left, depth + 1)
        # dfs(root, 0)
        # return ans
        if not root:
            return []
        ans = []
        q = deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans
# @lc code=end

