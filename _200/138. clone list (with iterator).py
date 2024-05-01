from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class LinkedListIterator:
    def __init__(self, head: 'Node'):
        self.current = head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            val = self.current.val
            self.current = self.current.next
            return val

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not(head):
            return None
        fakeHead = Node(0)
        clone = fakeHead
        node = head 
        dic = {}
        while node:
            clone.next = Node(node.val)
            clone = clone.next
            dic[node] = clone
            node = node.next 
        for node, clone in dic.items():
            if node.random:
                clone.random = dic[node.random]
        return fakeHead.next
    def printList(self, head: 'Optional[Node]'):
        if not(head): 
            print('None')
            return 
        iter = LinkedListIterator(head)
        print('=>'.join(str(val) for val in iter))
start_time = time.time()
app = Solution()   
root = app.copyRandomList(Node(1, Node(2, Node(3))))
app.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")