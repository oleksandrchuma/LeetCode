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
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                one_count = 0
                for i1 in range(max(i-1,0), min(i+2, n)):
                    for j1 in range(max(j-1,0), min(j+2, m)):
                        if board[i1][j1] >= 1 and (i1!=i or j1!=j):
                            one_count += 1
                if board[i][j]:
                    if one_count < 2:
                        board[i][j] = 2 
                    elif one_count <= 3:
                        board[i][j] = 1 
                    else:
                        board[i][j] = 2
                elif one_count == 3:
                    board[i][j] = -1
        for i in range(n):
            for j in range(m):
                board[i][j] = abs(board[i][j]) if board[i][j] != 2 else 0 
        #pprint.pprint(board)
start_time = time.time()
t = Solution()
root = t.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
