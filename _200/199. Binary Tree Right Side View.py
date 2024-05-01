import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
import math
import heapq
from collections import Counter
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not(root):
            return []

        dic = defaultdict(int)
        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop(0)
            dic[depth] = node.val
            depth += 1
            if node.left:
                stack.append((node.left, depth))
            if node.right:
                stack.append((node.right, depth))
        return [v for _,v in sorted(dic.items(), key=lambda x:x[0])]    
start_time = time.time()
app = Solution()
root = app.rightSideView(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4))))

#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

