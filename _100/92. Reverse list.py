from typing import List
from typing import Optional
import time
import math
from collections import Counter
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        fakeHead = ListNode()
        result = fakeHead
        i = 1
        while head is not None:
            if i == left:
                mid = []    
                while i <= right and head is not None:
                    mid.append(head.val)
                    i += 1
                    head = head.next

                while (len(mid) > 0):
                    result.next = ListNode(mid.pop())
                    result = result.next
            else:
                result.next = ListNode(head.val)
                result = result.next
                i += 1 
                head = head.next
        return fakeHead.next
    
    def print_linked_list(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")                     

start_time = time.time()
app = Solution()
app.print_linked_list(app.reverseBetween(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), 1, 5))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

