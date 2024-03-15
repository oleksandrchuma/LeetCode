import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import itertools
import heapq
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fakehead = ListNode()
        fakehead.next = head 
        removed = set()
        curr = head 
        dict = {0:fakehead}
        sum = 0
        while curr: 
            sum += curr.val 
            if sum not in dict or dict[sum] in removed: 
                dict[sum] = curr 
                curr = curr.next
            else: 
                start = dict[sum]
                end = curr.next 
                to_remove = start.next
                while to_remove and to_remove != end:
                    removed.add(to_remove)
                    next = to_remove.next
                    to_remove.next = None
                    to_remove = next 
                start.next = end
                curr = end  
        return fakehead.next
    def printList(self, head):
        while head:
            print(head.val, end="=>")
            head = head.next
        print("None")
start_time = time.time()
t = Solution()
root = t.removeZeroSumSublists(ListNode(1, ListNode(1, ListNode(-1))))
t.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

