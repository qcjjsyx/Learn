#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        nxt = cur.next if cur else None
        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = cur.next if cur else None
        return pre
# @lc code=end

