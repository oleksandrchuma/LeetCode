from typing import List
from typing import Optional
import time
from functools import lru_cache 
from collections import Counter

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:    
        if not(node):
            return None
        pairs = {node:Node(node.val)}
        stack = [node]
        while stack:
            curr = stack.pop()
            for child in curr.neighbors:
                if child not in pairs:
                    pairs[child] = Node(child.val)
                    stack.append(child)
        
        for item, cloned in pairs.items():
            cloned.neighbors = [pairs[neighbor] for neighbor in item.neighbors]
        return pairs[node]
start_time = time.time()
app = Solution()   
n1,n2,n3,n4 = Node(1), Node(2), Node(3), Node(4)
n1.neighbors = [n2,n4]
n2.neighbors = [n3,n1]
n3.neighbors = [n4,n2]
n4.neighbors = [n1,n3]

root = app.cloneGraph(n1)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
