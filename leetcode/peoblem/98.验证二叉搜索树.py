#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],left=-inf, right = inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left<x and x<right and self.isValidBST(root.left,left,x) and self.isValidBST(root.right,x,right)

# @lc code=end

