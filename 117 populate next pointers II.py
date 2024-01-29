from typing import List
from typing import Optional
import time
import math
from collections import Counter

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return root 
        l = root.left
        r = root.right 
        d = 0
        ls, rs = [], []
        while l is not None and r is not None:
            l.next = r 
            ls.append(l)
            rs.append(r)
            d += 1
            l = l.right if l.right else l.left
            r = r.left if r.left else r.right
            if l is None:
                l = ls.pop()
                while len(ls) < d and len(ls) > 0:
                    lp = ls.pop()    
                    if (lp.left and lp.left != l):
                        ls.append(lp)
                        l = lp.left 
                        while len(ls) < d and (l.right if l.right else l.left):
                            ls.append(l)
                            l = l.right if l.right else l.left
                    else: 
                        l = lp
                if len(ls) < d:
                    l = None
            if r is None:
                r = rs.pop()
                while len(rs) < d and len(rs) > 0:
                    rp = rs.pop()    
                    if (rp.right and rp.right != r):
                        rs.append(rp)
                        r = rp.right 
                        while len(rs) < d and (r.left if r.left else r.right):
                            rs.append(r)
                            r = r.left if r.left else r.right
                    else: 
                        r = rp
                if len(rs) < d:
                    r = None
        self.connect(root.left)
        self.connect(root.right)
        return root         
    
    #implement procedure that traverse tree and writes pairs value - next pointers
    def traverse(self, root: 'Optional[Node]', pairs: 'List[int, str]') -> 'None':
        if root is None:
            return 
        pairs.append([root.val, root.next.val if root.next is not None else "None"])
        self.traverse(root.left, pairs)
        self.traverse(root.right, pairs)
        return

start_time = time.time()
app = Solution()
l = Node(2, Node(1, Node(5, Node(11)), Node(1)))
r = Node(4, Node(3, None, Node(6)), Node(-1, None, Node(8, Node(11))))
root = Node(0, l, r)
app.connect(root)
list = []
app.traverse(root, list)
print(list)
print(root.left.left.left.next.val if root.left.left.left.next is not None else "None")
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

