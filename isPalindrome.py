from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrom(self, head: ListNode) -> bool:
        def isPal():
            for i in range(len(list)//2):
                if (list[i] != list[-i-1]):
                    return False
            return True
        if not(head):
            return head 
        list = []
        node = head
        while node: 
            list.append(node.val)
            node = node.next
        return isPal()     
    
    def printList(self, head):
        while head:
            print(head.val, end="=>")
            head = head.next
        print("None")   
            
start_time = time.time()
app = Solution()
root = app.isPalindrom(ListNode(1))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


