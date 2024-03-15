from typing import List
from typing import Optional
import time
import math
from collections import Counter
from functools import lru_cache
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:    
    def insertLow(self, head: ListNode, node: ListNode):
        while head.next and head.next.val < node.val:
            head = head.next 
        node.next = head.next 
        head.next = node 

    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head
        fakehead = ListNode(-10000, head)
        curr = head 
        while curr.next:
            while curr.next and curr.next.val > curr.val:
                curr = curr.next
            if curr.next:
                low = curr.next 
                curr.next = low.next 
                self.insertLow(fakehead, low)    
        return fakehead.next    
start_time = time.time()
app = Solution()
print(app.insertionSortList(ListNode(3, ListNode(2, ListNode(1)))))    
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

