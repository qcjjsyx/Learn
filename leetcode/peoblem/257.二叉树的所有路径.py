#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        path = []
        def backtrack(node):
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
                return
            
            if node.left:
                backtrack(node.left)
                path.pop()
            if node.right:
                backtrack(node.right)
                path.pop()
            
        backtrack(root)
        return ans
# @lc code=end

