import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        fakehead = ListNode(0, head)
        node = fakehead
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return fakehead.next
    def printList(self, head):
        while head:
            print(head.val, end="=>")
            head = head.next
        print("None")
start_time = time.time()
app = Solution()
root = app.removeElements(ListNode(2, ListNode(2, ListNode(3))), 2)
app.printList(root)
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

