from typing import List
from typing import Optional
import time
import math
import numpy
from collections import Counter
class Solution:
    def printMatrix(self, matrix):
        max_width = len(str(max(max(row) for row in matrix)))

        for row in matrix:
            for num in row:
                print(f"{num:>{max_width}}", end=" ")
            print()
        return 
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = {}
        if (endWord not in wordList):
            return 0
        add = 0
        if beginWord in wordList:
            add = 1
            wordList.remove(beginWord)
        wordList = [beginWord] + wordList
        m = [[] for _ in wordList]
        for i in range(len(wordList)):
            keys = set()
            for c in range(len(wordList[i])):
                key = wordList[i][:c]+"0"+wordList[i][c+1:]
                if key in keys:
                    continue
                keys.add(key)
                if (key not in dic):
                    dic[key] = []
                else:
                    for j in dic[key]:
                        m[i].append(j)
                        m[j].append(i)
                dic[key].append(i)
        visited = set() 
        queue = [0]
        weight = [0 for _ in wordList]
        while queue:
            v = queue[0]
            visited.add(v)
            queue.remove(v)
            for next in m[v]:
                if next not in visited:
                    queue.append(next)
                    if (weight[next] == 0):
                        weight[next] = weight[v] + 1
        print(weight)
        #self.printMatrix(m)
        return weight[wordList.index(endWord)] + 1 if weight[wordList.index(endWord)] > 0 else 0
start_time = time.time()
app = Solution()

root = app.ladderLength("talk", "tail", ["talk","tons","fall","tail","gale","hall","negs"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
