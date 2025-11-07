# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    d = ListNode()
    c = d
    carry = 0
    
    while l1 or l2 or carry:
        i = l1.val if l1 else 0
        j = l2.val if l2 else 0
        
        s = i + j + carry
        carry = (i + j) // 10
        
        c.next = ListNode(s % 10)
        c = c.next
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return d.next