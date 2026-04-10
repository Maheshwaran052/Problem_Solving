
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Using Hashtable
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visitedNodes = set()

#         curr = head

#         while curr:
#             if(curr in visitedNodes):
#                 return True
#             visitedNodes.add(curr)
#             curr = curr.next
#         return False

# using slow and fast pointers
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True
        return False
