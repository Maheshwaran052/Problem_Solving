# Definition for singly-linked list.
import heapq

""" merge(0,2)
  ↓
merge(0,1)
  ↓
merge(0,0) ✅ return
  ↓
merge(1,1) ✅ return
  ↓
merge L1 + L2 ✅
  ↓
merge(2,2) ✅ return
  ↓
merge (L1+L2) + L3 ✅ """


""" Full flow

| Step | Function Call         | left | right | l1 value             | l2 value   |
| ---- | --------------------- | ---- | ----- | -------------------- | ---------- |
| 1    | merge(0,2)            | 0    | 2     | —                    | —          |
| 2    | merge(0,1)            | 0    | 1     | —                    | —          |
| 3    | merge(0,0)            | 0    | 0     | returns L1           | —          |
| 4    | merge(1,1)            | 1    | 1     | —                    | returns L2 |
| 5    | merge(0,1) resumes    | 0    | 1     | L1                   | L2         |
| 6    | mergeTwoLists(L1, L2) | —    | —     | → M1 = [1→1→2→3→4→5] | —          |
| 7    | merge(2,2)            | 2    | 2     | —                    | returns L3 |
| 8    | merge(0,2) resumes    | 0    | 2     | M1                   | L3         |
| 9    | mergeTwoLists(M1, L3) | —    | —     | → Final              | —          | """


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Using Divide and conqueor, recursion,merge sort
class Solution:    
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]

        mid = (left + right) // 2

        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)

        return self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next
    
# Using heap

class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Step 1: push first node of each list
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))

        # Dummy node to build result
        dummy = ListNode(0)
        curr = dummy

        # Step 2: process heap
        while heap:
            val, i, node = heapq.heappop(heap)

            # attach smallest node
            curr.next = node
            curr = curr.next

            # push next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
        