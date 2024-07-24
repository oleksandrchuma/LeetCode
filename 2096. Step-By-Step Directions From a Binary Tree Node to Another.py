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
import numpy 
import pprint

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node, val):
            if not(node):
                return (False, [])

            if node.val == val:
                return (True, [])
            if node.left:
                found, path = find(node.left, val)
                if found:
                    path.insert(0, "L")
                    return True, path
            if node.right:
                found, path = find(node.right, val)
                if found:
                    path.insert(0, "R")
                    return True, path
            return (False, [])
        if not(root):
            return ""
        _, path1 = find(root, startValue)
        _, path2 = find(root, destValue)
        prefix = 0
        while prefix < min(len(path1), len(path2)) and path1[prefix] == path2[prefix]:
            prefix += 1    
        path1 = path1[prefix:]
        path2 = path2[prefix:]

        return "U"*len(path1)+("".join(path2)) 
start_time = time.time()
t = Solution()
#[5,1,2,3,null,6,4]
root = t.getDirections(TreeNode(5, TreeNode(1, TreeNode(3)), TreeNode(2, TreeNode(6), TreeNode(4))), 5, 1)

print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
