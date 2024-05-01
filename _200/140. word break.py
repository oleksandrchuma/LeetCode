from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = [[] for _ in s]
        for i in range(len(s)):
            for word in wordDict:
                wordlen = len(word)
                if wordlen == i+1 or (i+1 > wordlen and len(result[i-wordlen])):
                    if (s[i+1-wordlen:i+1] == word):
                        if i+1 > wordlen:
                            result[i] += [sentence+[word] for sentence in result[i-wordlen]]
                        else:
                            result[i] += [[word]]
        return [' '.join(sentence) for sentence in result[-1]]
start_time = time.time()
app = Solution()   
root = app.wordBreak("leetcode", ["leet","code"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")