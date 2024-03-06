from typing import List
from typing import Optional
from collections import defaultdict
import time
import math

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dict = defaultdict(int)
        for i in range(len(s)-10+1):
            dict[s[i:i+10]] += 1
        return [k for k,v in dict.items() if v > 1]
start_time = time.time()
app = Solution()
root = app.findRepeatedDnaSequences("AAAAAAAAAAA")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

