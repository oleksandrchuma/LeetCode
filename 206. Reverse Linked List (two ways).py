import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head):
            return head 
        node = head
        prev = None 
        while node.next:
            t = node.next 
            node.next = prev
            prev = node
            node = t
        node.next = prev 
        return node     
    
    def reverseListRec(self, head, tail): 
        if not(head):
            return tail
        next = head.next
        head.next = tail
        return self.reverseListRec(next, head)
     
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverseListRec(head, None)     
    
    def printList(self, head):
        while head:
            print(head.val, end="=>")
            head = head.next
        print("None")         
start_time = time.time()
app = Solution()

root = app.reverseList2(ListNode(1, ListNode(2, ListNode(3))))
app.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

