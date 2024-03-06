from typing import List
from typing import Optional
from collections import defaultdict
import time
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n
    def setNext(self, n):
        self.next = n 

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False 
        prev = head 
        node = head.next
        head.next = None  
        while node is not None:
            x = node.next 
            node.next = prev 
            prev = node 
            node = x 
            
        return prev == head 
            
start_time = time.time()
app = Solution()
tail = ListNode(3, None)
head = ListNode(1, ListNode(2,tail))
tail.next = head

root = app.hasCycle(ListNode(5, head))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

