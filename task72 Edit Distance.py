from typing import List
from typing import Optional
import time
import math

class Solution:
    dict = {}
    def get_char_indexes(self, s, char):
        return [i for i, c in enumerate(s) if c == char]

    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            (word1, word2) = (word2, word1)
        l1 = len(word1)
        l2 = len(word2)
        if (l2 == 0):
            return l1
        
        if l2 == 1:
            return l1-1 if word2[0] in word1 else l1
        
       # if l1 == l2:
        #    return sum(0 if word1[i] == word2[i] else 1 for i in range(l1))
        #
        mind = l1
        for i in range(l2):
            if i >= mind: 
                return mind
            for pos in self.get_char_indexes(word1, word2[i]):
                if (pos + abs((l1 - pos) - (l2 - i)) >= mind):
                    break
                #if l1 - pos >= l2 - i:
                d = max(pos, i) + self.minDistance(word1[pos+1:l1], word2[i+1:l2])
                if d < mind: 
                    mind = d           
        return mind

start_time = time.time()
print(Solution().minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

