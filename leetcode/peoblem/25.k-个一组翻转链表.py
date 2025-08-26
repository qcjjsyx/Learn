#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        n = 0
        while p:
            p = p.next
            n += 1
        if n < k:
            return head
        pivot = ListNode(next=head)
        p0 = pivot
        while n >= k:
            nxt = p0.next
            pre =None
            cur = p0.next
            for _ in range(k):
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
            n -= k
        return pivot.next
# @lc code=end

