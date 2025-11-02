# https://leetcode.com/problems/remove-nodes-from-linked-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    p = None
    c = head
    
    while c:
        n = c.next
        c.next = p
        p = c
        c = n
    
    return p
        
def removeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    head = reverseLinkedList(head)
    
    c = head
    
    while c.next:
        if c.val > c.next.val:
            c.next = c.next.next
        else:
            c = c.next
            
    head = reverseLinkedList(head)
    
    return head # (207 ms)