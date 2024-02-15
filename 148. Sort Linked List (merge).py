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
    def skip(self, head: Optional[ListNode], len: int) -> Optional[ListNode]:
        for i in range(len):
            if head:
                head = head.next
        return head
    
    def mergeLists(self, left: Optional[ListNode], leftLen: int, 
                         right: Optional[ListNode], rightLen: int) -> Optional[ListNode]:
        fakehead = ListNode()
        curr = fakehead
        while leftLen or rightLen:
            if left and leftLen and ((rightLen and right and left.val <= right.val) or not rightLen):
                curr.next = left
                curr = curr.next 
                left = left.next
                leftLen -= 1
            elif right and rightLen:
                curr.next = right
                curr = curr.next 
                right = right.next
                rightLen -= 1
        curr.next = None
        return fakehead.next 
    
    def mergeSort(self, head: Optional[ListNode], len: int) -> Optional[ListNode]:
        if len == 1 and head:
            head.next = None
            return head
        rightHead = self.skip(head, len//2)
        left = self.mergeSort(head, len//2)
        right = self.mergeSort(rightHead, len-len//2)
        return self.mergeLists(left, len//2, right, len-len//2)
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        len = 0
        node = head  
        while node:
            len +=1
            node = node.next

        return self.mergeSort(head, len)
    
    def printList(self, root):
        while root:
            print(root.val, end = " ")
            root = root.next 
        print()
start_time = time.time()
app = Solution()

data = [4, 3, 2, 1]
data = reversed([i for i in range(1000)])
root = ListNode()
tail = root 
for x in data: 
    tail.next = ListNode(x)
    tail = tail.next
    
root = root.next
root = app.sortList(root)
app.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

