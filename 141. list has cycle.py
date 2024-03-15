from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

# Definition for a Node.
class ListNode:
    def __init__(self, x: int, next: 'Optional[ListNode]' = None, random: 'Optional[ListNode]' = None):
        self.val = int(x)
        self.next = next

class LinkedListIterator:
    def __init__(self, head: 'ListNode'):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            val = self.current
            self.current = self.current.next
            return val

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if (head is None):
            return False
        s = set()
        while head:
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False
    def printList(self, head: 'Optional[ListNode]'):
        if not(head): 
            print('None')
            return 
        iter = LinkedListIterator(head)
        print('=>'.join(str(val) for val in iter))
start_time = time.time()
app = Solution()   
root = app.hasCycle(ListNode(1, ListNode(2, ListNode(3))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")