from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted([(v,c) for (c,v) in enumerate(score)], reverse=True)
        result = ["" for _ in score]
        for i in range(len(sorted_score)):
            _, order = sorted_score[i]
            if i == 0:
                result[order] = "Gold Medal"
            elif i == 1:
                result[order] = "Silver Medal"
            elif i == 2:
                result[order] = "Bronze Medal"
            else: 
                result[order] = str(i+1)
        return result
start_time = time.time()
app = Solution()
root = app.findRelativeRanks([10,3,8,9,4])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


