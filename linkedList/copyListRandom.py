
# Definition for a Node.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create mapping
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Assign next and random
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new[head]