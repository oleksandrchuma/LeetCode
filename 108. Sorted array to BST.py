from typing import List
from typing import Optional
import time
import math
from collections import Counter

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def toVine(self, root: Optional[ListNode]):
        size = 0
        vine = TreeNode()
        current = vine
        while root:
            current.right = TreeNode(root.val)
            current = current.right
            root = root.next
            size += 1
        return (vine, size)
    
    def sortedListToBST(self, root: Optional[ListNode]) -> Optional[TreeNode]:
        vine,size = self.toVine(root)
        leaves = size + 1 - int(pow(2, int(math.log2(size+1))))
        self.compress(vine, leaves)
        print(self.levelOrder(vine))
        size -= leaves
        while size > 1:
            size //= 2
            self.compress(vine, size)
            print(self.levelOrder(vine))
        return vine.right
        
    def compress(self, current: TreeNode, count: int):
        for _ in range(count):
            if current.right is None:
                return 
            child = current.right
            current.right = child.right
            current = current.right
            child.right = current.left
            current.left = child 

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []
        result = []
        stack = [root]
        while len(stack):
            next = []
            result.append([])
            for node in stack:
                result[-1].append(node.val)
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)    
            stack = next
        return result
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        result = self.inorderTraversal(root.left)
        result.append(root.val)
        result += self.inorderTraversal(root.right)
        return result
    
start_time = time.time()
app = Solution()
print(app.inorderTraversal(app.sortedListToBST(ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

