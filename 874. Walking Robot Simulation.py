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
import pprint
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = set([(x[0], x[1]) for x in obstacles])
        dirs = [[0,1], [1,0],[0,-1],[-1,0]]
        dir = 0
        result = 0
        x, y = 0, 0
        for command in commands:
            if command == -1:
                dir = (dir+1)%4
            elif command == -2:
                dir = (dir-1)%4
            else:
                for _ in range(command):
                    nx = x+dirs[dir][0]
                    ny = y+dirs[dir][1]
                    if (nx,ny) not in obstacles_set:
                        x = nx
                        y = ny 
                    else:
                        break
                result = max(x*x+y*y, result)
        return result 
start_time = time.time()

t = Solution()
#root = t.removeDuplicateLetters("cbacdcbc")
root = t.robotSim([4,-1,4,-2,4], [[2,4]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
