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
        def bft(node, level):
            if not(node):
                return 
            enum.append((node, level))
            if node.val == p.val or node.val == q.val:
                pos.append(len(enum)-1)
            bft(node.left, level+1)
            bft(node.right, level+1)
        enum = []
        pos = []
        bft(root, 1)
        l = min(pos)
        r = max(pos)
        level = enum[r][1] 
        for i in range(l+1, r):
            if enum[i][1] < level:
                level = enum[i][1]
        for i in range(l,-1,-1):
            if enum[i][1]<level:
                return enum[i][0]
        return TreeNode(-1)
    def build(self, nodes: List[Optional[int]]) -> TreeNode:    
        if (len(nodes) == 0 or nodes[0] is None):
            return None
        root = TreeNode(nodes[0])
        queue = []
        queue.append(root)
        i = 1
        while i < len(nodes):
            node = queue.pop()
            if nodes[i] is not None:
                node.left = TreeNode(nodes[i] or 0)    
                queue.insert(0, node.left)
            i+=1
            if i >= len(nodes):
                    break
            if nodes[i] is not None:
                node.right = TreeNode(nodes[i] or 0)
                queue.insert(0, node.right)
            i+=1
        
        return root
start_time = time.time()
t = Solution()
root = t.lowestCommonAncestor(t.build([3,5,1,6,2,0,8,None,None,7,4]), TreeNode(5), TreeNode(4))
print(root.val)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

'''
(x+n)(n-x+1)=x(x+1) 
n2-x2+n = x2
x = sqrt((n2+n)/2)

'''