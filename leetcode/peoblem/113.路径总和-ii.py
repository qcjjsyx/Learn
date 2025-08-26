#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root is None:
            return ans
        path = [root.val]
        def dfs(node,current_sum):
            if current_sum == targetSum and not node.left and not node.right:
                ans.append(path.copy())
                return
            if node.left:
                path.append(node.left.val)
                dfs(node.left, current_sum + node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right, current_sum + node.right.val)
                path.pop()
        dfs(root, root.val)
        return ans
# @lc code=end

