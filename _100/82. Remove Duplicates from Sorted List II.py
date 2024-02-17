from typing import List
from typing import Optional
import time

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        fakehead = ListNode()
        write = fakehead
        read = head 
        curr = read.val
        duplicate = 0

        while read is not None:
            if read.next is None or read.next.val != curr:
                if not(duplicate):
                    write.next = ListNode(curr, None)
                    write = write.next
                curr = read.next.val if read.next is not None else -1
                duplicate = 0
            else:
                duplicate = 1 
            read = read.next

        return fakehead.next
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        fakehead = ListNode()
        prev = fakehead
        while (curr):
            store = []
            while (curr and len(store) < k):
                store.append(curr)
                curr = curr.next
            if (len(store) == k):
                while(len(store) > 0):
                    prev.next = store.pop()
                    prev = prev.next
                prev.next = curr    
        return fakehead.next if fakehead.next else head
    
    def print_linked_list(self, head):
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        
list1 = ListNode(1, ListNode(4, ListNode(4, ListNode(3, ListNode(2, ListNode(2))))))
start_time = time.time()
res=Solution().deleteDuplicates(list1)
Solution().print_linked_list(res)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
