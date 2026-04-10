from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if(l1.val < l2.val):
                curr.next = l1
                curr = l1
                l1 = l1.next
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
        #Attach remaining
        if l1:
            curr.next = l1
        else:
            curr.next = l2
        
        return dummy.next
                

                
            