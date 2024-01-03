from typing import List
from typing import Optional
import time
from collections import Counter
import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        char_count = Counter(t)
        rez = None
        start = 0; end = 0
        while start < len(s) and s[start] not in char_count:
            start+=1
        end = start    
        while end < len(s):
            c = s[end]
            if (c in char_count):
                char_count[c] -= 1
                if all(value <= 0 for value in char_count.values()):
                    while s[start] not in char_count or char_count[s[start]] < 0:
                        if (s[start] in char_count):
                            char_count[s[start]] += 1
                        start += 1
                    if (rez is None or len(rez) > end - start + 1):
                        rez = s[start:end+1]
            end += 1 
        return rez if rez is not None else '' 
start_time = time.time()
print(Solution().minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

