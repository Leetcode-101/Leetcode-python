#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        _carry = 0
        head: ListNode = None
        tail: ListNode = None
        while l1 or l2:
            _val_1, _val_2 = 0, 0
            if l1:
                _val_1 = l1.val
                l1 = l1.next
            if l2:
                _val_2 = l2.val
                l2 = l2.next 
            _sum = _val_1 + _val_2 + _carry

            _val = _sum % 10
            _carry = _sum // 10
            if not head:
                head = ListNode(val=_val)
                tail = head
            else:
                tail.next = ListNode(val=_val)
                tail = tail.next
        if _carry:
            tail.next = ListNode(val=_carry)
        return head

# @lc code=end
