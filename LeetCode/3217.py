# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def modifiedList(nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)

    p = ListNode(0)
    p.next = head

    c = p
    
    while c.next:
        if c.next.val in nums:
            c.next = c.next.next
        else:
            c = c.next
    
    return p.next # (135 ms)