from typing import List
from typing import Optional
from collections import defaultdict
import time
import math

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        def doStep(curr, last, power): 
            while curr < last and tokens[curr+1] <= power:
                power -= tokens[curr+1]
                curr += 1
            return curr, power
        score = 0
        tokens.sort()
        last = len(tokens)-1
        curr,power = doStep(-1, last, power)
        score = curr+1
        if score == 0:
            return 0
        while curr+1 < last:
            power += tokens[last]
            last -= 1 
            next,power = doStep(curr, last, power)
            if next > curr:
                score += next - curr - 1
                curr = next
            else:
                break
        return score 
start_time = time.time()
app = Solution()
root = app.bagOfTokensScore([71,55,82], 54)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

