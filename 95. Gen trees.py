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

class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result
    
    def gen(self, nums: List[int]) -> List[Optional[TreeNode]]:
        if len(nums) == 0:
            return [None]
        result = []
        for i in range(len(nums)):
            root = nums[i]
            leftTrees = self.gen(nums[0:i])
            rightTrees =self.gen(nums[i+1:]) if i < len(nums) - 1 else [None]
            for left in leftTrees:
                for right in rightTrees:
                    result.append(TreeNode(root, left, right))    
        return result
    
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = [x + 1 for x in range(n)]
        return self.gen(nums)

start_time = time.time()
app = Solution()
print(len(app.generateTrees(3)))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

