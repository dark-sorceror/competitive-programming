# https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

from typing import Optional

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def modifiedList(nums: list[int], head: Optional[ListNode]) -> Optional[ListNode]:
    nums = set(nums)

    p = ListNode(0)
    p.next = head

    current = p
    
    while current.next:
        if current.next.val in nums:
            current.next = current.next.next
        else:
            current = current.next
    
    return p.next