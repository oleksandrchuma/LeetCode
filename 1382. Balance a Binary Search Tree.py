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
    def buildTree(self, nums, start, end) -> TreeNode:
        mid = (start + end)//2
        root = TreeNode(nums[mid])
        if (mid > start):
            root.left = self.buildTree(nums, start, mid-1)
        if (mid < end):
            root.right = self.buildTree(nums, mid+1, end)
        return root
         
    def balanceBST(self, root: TreeNode) -> TreeNode:
        visited = set()
        stack = [root]
        nums = []
        while stack:
            node = stack.pop()
            if node in visited:
                nums.append(node.val)
            else: 
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                if (node.left):
                    stack.append(node.left)
                visited.add(node)
        print(nums)

        return self.buildTree(nums, 0, len(nums)-1)         
start_time = time.time()
t = Solution()
root = t.balanceBST(TreeNode(1, TreeNode(0), TreeNode(2, None, TreeNode(3, None, TreeNode(4)))))
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
