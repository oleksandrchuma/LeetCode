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
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        if not(root):
            return ""
        result = []    
        visited = set()
        stack = [root]
        while (len(stack)>0):
            node = stack.pop()
            if node in visited:
                result.append(f"{node.val}+{(1 if node.left else 0) + (2 if node.right else 0)}")
            else:
                visited.add(node)
                stack.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return ','.join(result)
    def deserialize(self, data):
        if data == "":
            return None
        tokens = data.split(',')
        stack = []
        for token in tokens:
            args = token.split('+')
            val = int(args[0])
            c = int(args[1])
            node = TreeNode(val)
            if c%2 == 1:
                node.left = stack.pop()
            if c >= 2: 
                node.right = stack.pop()
            
            stack.append(node)
        return stack.pop()
# Your Codec object will be instantiated and called as such:
start_time = time.time()
ser = Codec()
deser = Codec()

#ans = deser.deserialize(ser.serialize(root))
data = ser.serialize(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))))
root = deser.deserialize(data)

#t = Solution()
#root = t.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
#pprint.pprint(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
