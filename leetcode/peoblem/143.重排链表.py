#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        pre,cur = None,mid
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0,p1 = head,pre
        while p1 and p1.next:
            nxt0 = p0.next
            nxt1 = p1.next
            p0.next = p1
            p1.next = nxt0
            p0 = nxt0
            p1 = nxt1
# @lc code=end

