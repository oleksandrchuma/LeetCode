from typing import List
from typing import Optional
import time
import math
from collections import Counter
class Item:
        def __init__(self, key: int, val: int, next: 'Optional[Item]'= None, prev: 'Optional[Item]'= None):
            self.val = val
            self.prev = prev
            self.next = next
            self.key = key 

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.first = None
        self.last = None

    def append_to_queue(self, item):
        if self.last:
            self.last.next = item
        item.prev = self.last    
        item.next = None 
        self.last = item
        if (not self.first):
            self.first = item

    def remove_from_queue(self, item):
        if item.prev:
            item.prev.next = item.next 
        else: 
            self.first = item.next 
        if item.next:
            item.next.prev = item.prev 
        else: 
            self.last = item.prev
    
    def refresh_queue(self, item):
        self.remove_from_queue(item)
        self.append_to_queue(item)

    def get(self, key: int) -> int:
        result = self.dict.get(key, None)
        if result: 
            self.refresh_queue(result)
        return result.val if result else -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            item = self.dict[key]
            item.val = value
            self.refresh_queue(item)
        else:
            item = Item(key, value)
            self.dict[key] = item
            self.append_to_queue(item)
            
            if len(self.dict) > self.capacity:
                if (self.first):
                    del(self.dict[self.first.key])
                self.remove_from_queue(self.first)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
start_time = time.time()
#app = Solution()
lRUCache = LRUCache(2);
lRUCache.put(1, 1); #// cache is {1=1}
lRUCache.put(2, 1); #// cache is {1=1, 2=2}
lRUCache.put(2, 2); #// cache is {1=1, 2=2}
print(lRUCache.get(2));    #// return 1
lRUCache.put(3, 3); #// LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lRUCache.get(2));    #// returns -1 (not found)
lRUCache.put(4, 4); #// LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1));    #// return -1 (not found)
print(lRUCache.get(3));    #// return 3
print(lRUCache.get(4));    #// return 4
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

