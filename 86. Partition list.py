from typing import List
from typing import Optional
import time
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lowhead = ListNode()
        highhead = ListNode()
        low = lowhead
        high = highhead 
        while head is not None:
            if head.val < x:
                low.next = ListNode(head.val)
                low = low.next
            else:
                high.next = ListNode(head.val)
                high = high.next    
            head = head.next
        low.next = highhead.next
        return lowhead.next
    
    def print_linked_list(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
start_time = time.time()
Solution().print_linked_list(Solution().partition(ListNode(1, ListNode(4, ListNode(4, ListNode(3, ListNode(2, ListNode(2)))))), 3))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

