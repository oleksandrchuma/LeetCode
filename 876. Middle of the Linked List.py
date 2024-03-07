from typing import List
from typing import Optional
from collections import defaultdict
import time
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head 
        p2 = head
        if not p1 or not p1.next:
            return p1 
        while p1 and p1.next:
            p1 = p1.next.next if p1.next else None
            p2 = p2.next if p2 else None 
        return p2 
start_time = time.time()
app = Solution()


root = app.middleNode(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode)))))
print(root.val)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

