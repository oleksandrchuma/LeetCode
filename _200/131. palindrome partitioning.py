from typing import List
from typing import Optional
import time
from collections import Counter
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        for i in range(len(s)//2):
            if s[i] != s[-(i+1)]:
                return False
        return True
    
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [] 
        result = [[] for _ in s]
        result[0] = [[s[0]]]
        for i in range(1, len(s)):
            if (self.isPalindrome(s[:i+1])):
                result[i].append([s[:i+1]])
            for j in range(1, i+1):
                sub = s[j:i+1]
                if (self.isPalindrome(sub)):
                    result[i] += [prev + [sub] for prev in result[j-1]]

        return result[-1]
    
    def minCut(self, s: str) -> int:
        return min([len(split) for split in self.partition(s)]) - 1
start_time = time.time()
app = Solution()   

root = app.minCut("ababababababababababababcbabababababababababababa")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
