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
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nums = self.inorderTraversal(root)
        result = True
        if (len(nums)) > 1: 
            for i in range(len(nums) - 1):
                if nums[i] >= nums[i+1]:
                    result = False
                    break
        return result
   
    def swapValue(self, root: Optional[TreeNode], x: int, y: int):
        if root is None: return 
        if root.val == x:
            root.val = y
        elif root.val == y:
            root.val = x
        self.swapValue(root.left, x, y)
        self.swapValue(root.right, x, y)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        nums = self.inorderTraversal(root)
        k = 0; p = len(nums)-1
        ik = 0
        for i in range(len(nums) - 1):
                if nums[i] >= nums[i+1]:
                    k = nums[i]
                    ik = i
                    break

        for i in range(len(nums)-1,0,-1):
            if nums[i] < nums[i-1]:
                p = nums[i]
                break
        print(k, p)
        self.swapValue(root, k, p)

    def traverseByLevels(self, root: Optional[TreeNode], level: int, dict):
        if root is None: 
            return 
        if level not in dict:
            dict[level] = []
        dict[level].append(root.val)
        self.traverseByLevels(root.left, level+1, dict)
        self.traverseByLevels(root.right, level+1, dict)


    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dict = {}
        self.traverseByLevels(root, 0, dict)
        if len(dict) == 0:
            return []        
        return [dict[i] for i in range(len(dict))]
    
start_time = time.time()
app = Solution()
tree = TreeNode(1, TreeNode(3, TreeNode(4), TreeNode(2)))
print(app.levelOrder(tree))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

