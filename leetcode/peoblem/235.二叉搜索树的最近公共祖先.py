#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if p.val < root.val and q.val > root.val:
            return root
        if p.val <root.val and q.val <root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val >root.val and q.val >root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
# @lc code=end

