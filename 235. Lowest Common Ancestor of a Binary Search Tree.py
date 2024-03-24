import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
    # Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val:
            return root 
        if (root.val>p.val)^(root.val>q.val):
            return root 
        if root.val>p.val and root.val>q.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q) 
        if root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
start_time = time.time()
t = Solution()
root = t.lowestCommonAncestor(TreeNode(1), TreeNode(1), TreeNode(2))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''