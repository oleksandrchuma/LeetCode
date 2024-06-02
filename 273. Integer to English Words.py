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
class Solution:
    def __init__(self) -> None:
        self.ones = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
        }
        self.tens = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        self.thousands = {
            0: "",
            1: "Thousands",
            2: "Millions",
            3: "Billions"
        }

    def convertThousand(self, part, t_index):
            hundreds = part//100
            s = ''
            ends_with_one = False
            if (hundreds > 0):
                s = f"{self.ones[hundreds]} Hundred"
            low = part%100
            if (low > 0):
                if (s != ''):
                    s += ' '
                if low < 20: 
                    s += self.ones[low]
                    ends_with_one = low == 1
                else:
                    s+= f"{self.tens[low//10]}"
                    if (low%10 > 0):
                        s += ' ' + self.ones[low%10]
                    ends_with_one = low%10 == 1
            if t_index > 0:
                s += ' ' + (self.thousands[t_index][:-1] if ends_with_one else self.thousands[t_index][:-1])
            return s 
    
    def numberToWords(self, num: int) -> str:
        
        res = ''
        t_index = 0
        if (num == 0):
            return "Zero"
        while num > 0:
            part = num % 1000 
            if part > 0:
                if res != '':
                    res = ' ' + res
                res = f"{self.convertThousand(part, t_index)}" + res 
            num = num//1000
            t_index += 1
        return res
start_time = time.time()
t = Solution()
root = t.numberToWords(1234567)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
