from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def wordBreakInternal(str) -> bool: 
            if (len(str) == 0):
                return True
            for word in wordDict:
                wordlen = len(word)
                if wordlen <= len(str):
                    if (str[-wordlen:] == word and wordBreakInternal(str[:-wordlen])):
                        return True
            return False
        return wordBreakInternal(s)

        
'''    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [0 for _ in s]
        for i in range(len(s)):
            for word in wordDict:
                wordlen = len(word)
                if wordlen == i+1 or (i+1 > wordlen and result[i-wordlen]==1):
                    if (s[i+1-wordlen:i+1] == word):
                        result[i] = 1
                        break
                 
        return result[-1] == 1
'''
start_time = time.time()
app = Solution()   
root = app.wordBreak("leetcode", ["leet","code"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")