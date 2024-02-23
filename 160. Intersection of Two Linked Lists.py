from typing import List
from typing import Optional
import time
import math
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
         self.val = x
         self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next 
            return prev
        def tail(head):
            res = head 
            while res and res.next:
                res = res.next 
            return res
        def skip(head, n):
            res = head 
            while n > 0:
                res = res.next
                n-=1 
            return res
        def listLen(head):
            res = 0
            while head:
                res += 1
                head = head.next
            return res 
        if not headA or not headB:
            return ListNode(0) 
        if headA == headB:
            return headA
        a = listLen(headA)
        b = listLen(headB)
        tailB = tail(headB)
        if tailB == headA:
            return headA 
        
        headA = reverse(headA)
        if tailB == headA:
            headA = reverse(headA)
            return tailB 
        if tailB == tail(headB):
            headA = reverse(headA)
            return None
        c = listLen(headB)
        tailLen = (a+b-c+1)//2
        headA = reverse(headA)
        return skip(headA, a-tailLen)

    def printList(self, head):
        while(head):
            print(head.val, end='->')
            head = head.next
        print('None')


start_time = time.time()
app = Solution()
root = ListNode(1, None)
root = app.getIntersectionNode(ListNode(5, root), ListNode(3, root))
app.printList(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

