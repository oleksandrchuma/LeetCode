import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import heapq 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.left = None
        self.right = None
        self.mode = 0
        self.root = root 

    def leftIter(self):
        if self.left is None and self.root:
            self.left = BSTIterator(self.root.left)
        
        return self.left

    def rightIter(self):
        if self.right is None and self.root:
            self.right = BSTIterator(self.root.right)
        return self.right
    
    def next(self) -> int:
        if self.hasNext():
            if self.mode == 0:
                left = self.leftIter()
                return left.next() if left else -1
            if self.mode == 1:
                self.mode = 2
                return self.root.val if self.root else -1
            if self.mode == 2:
                right = self.rightIter()
                return right.next() if right else -1
        return -1
    
    def hasNext(self) -> bool:
        if self.mode == 0:
            left = self.leftIter()
            if not left or not left.hasNext():
                self.mode = 1
            else: 
                return True
        if self.mode == 1:
            if not self.root:
                self.mode = 2
            else:
                return True
        if self.mode == 2:
            right = self.rightIter()
            if not right or not right.hasNext():
                self.mode = 3
            else: 
                return True
        return False
        
# Your BSTIterator object will be instantiated and called as such:

obj = BSTIterator(None)
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.hasNext())
        
#app = Solution()
start_time = time.time()
#root = app.titleToNumber("AA")
#print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

