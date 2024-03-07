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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None
        list = [_ for _ in LinkedListIterator(head)]
        l, r = 0, len(list)-1
        fakeHead = ListNode(0)
        node = fakeHead
        while (l <= r):
            node.next = list[l]
            node = node.next
            l += 1
            if (l > r):
                break
            node.next = list[r]
            node = node.next
            r -= 1
        node.next = None
    def printList(self, head: 'Optional[ListNode]'):
        if not(head): 
            print('None')
            return 
        iter = LinkedListIterator(head)
        print('=>'.join(str(val.val) for val in iter))
start_time = time.time()
app = Solution()   
r = ListNode(1, ListNode(2, ListNode(3)))
result = app.reorderList(r)
app.printList(r)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")