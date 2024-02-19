import ast
import time
from typing import List
from collections import Counter
from functools import lru_cache
import heapq
from collections import deque

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_usage = [0 for _ in range(n)]
        free_rooms = [i for i in range(n)]
        booking = []
        meetings.sort(key=lambda item: item[0])
        heapq.heapify(free_rooms)
        for m in meetings:
            start, end = m[0], m[1]
            while booking and booking[0][0] <= start:
                (_, room) = heapq.heappop(booking)
                heapq.heappush(free_rooms, room)
            if free_rooms:
                room = heapq.heappop(free_rooms)
            else:
                (prev, room) = heapq.heappop(booking)
                end = prev + (end - start)
            heapq.heappush(booking, (end, room))
            room_usage[room] += 1
        r,u = max(enumerate(room_usage), key=lambda item: item[1])
        return r
app = Solution()
with open('input.txt', 'r') as file:
    content = file.read()
array = ast.literal_eval(content)

start_time = time.time()
root = app.mostBooked(100, array)
#root = app.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

