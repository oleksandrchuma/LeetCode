from typing import List
from typing import Optional
import time
import math
from collections import Counter

class Solution:
    cache = {}
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n == 0: 
            return False
        if n == 1:
            return s1[0] == s2[0]
        if (s1, s2) in self.cache:
            return self.cache[(s1,s2)]
        c1 = Counter()
        c2 = Counter()
        for i in range(n-1):
            c1[s1[i]] += 1
            c2[s2[i]] += 1
            if c1 == c2: 
                if (self.isScramble(s1[:i+1], s2[:i+1]) and self.isScramble(s1[i+1:], s2[i+1:])):
                    self.cache[(s1, s2)] = True
                    return True
        c1 = Counter()
        c2 = Counter()

        for i in range(len(s1)-1):
            c1[s1[i]] += 1
            c2[s2[n-i-1]] += 1
            if c1 == c2: 
                if (self.isScramble(s1[:i+1], s2[n-i-1:]) and self.isScramble(s1[i+1:], s2[:n-i-1])):
                    self.cache[(s1, s2)] = True
                    return True
        self.cache[(s1, s2)] = False
        return False
start_time = time.time()
print(Solution().isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

