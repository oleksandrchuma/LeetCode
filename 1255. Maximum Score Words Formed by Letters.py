import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
import numpy 
import pprint

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counter = Counter(letters)
        result = 0
        max_result = 0
        used_words = [0 for _ in words]
        def getWord(word):
            wc = Counter(word)
            for chr, chr_count in wc.items():
                if counter[chr] < chr_count:
                    return False
            for chr, chr_count in wc.items():
                counter[chr] -= chr_count
            return True
        
        def returnWord(word):
            wc = Counter(word)
            for chr, chr_count in wc.items():
                counter[chr] += chr_count

        def wordPrice(word):
            return sum([score[ord(c)-ord('a')] for c in word])
        
        def rec(ind):
            nonlocal result
            nonlocal max_result
            if ind == len(words):
                if result > max_result:
                    max_result = result 
                return
            repeat_count = 0
            while repeat_count==0 and getWord(words[ind]):
                repeat_count+=1
                used_words[ind] = 1
                result += wordPrice(words[ind])
            rec(ind+1)
            while repeat_count > 0:
                used_words[ind] -= 1
                result -= wordPrice(words[ind])
                returnWord(words[ind])
                repeat_count -= 1
                rec(ind+1)
        rec(0)
        return max_result
                            
start_time = time.time()
t = Solution()
[21,21,18,12,21]
root = t.maxScoreWords(["add","dda","bb","ba","add"], ["a","a","a","a","b","b","b","b","c","c","c","c","c","d","d","d"], 
                       [3,9,8,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
