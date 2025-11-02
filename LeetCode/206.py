# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next
        
def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    p = None
    c = head
    
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    
    return p # (0 ms)