from typing import List
from typing import Optional
import time
import math
from functools import lru_cache 
from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        def split_number_into_bits(number):
            sign = 0 if number >= 0 else 1 
            binary_representation = bin(abs(number))[2:]
            bits = [int(bit) for bit in reversed(binary_representation)]
            if sign:
                bits = [bits[i] if i < len(bits) else 0 for i in range(33)]
                bits[-1] = 1
            return bits
        def bits_into_number(bits):
            last = 0
            sign = -1 if bits[-1] else 1
            bits[-1] = 0

            for i in range(len(bits)):
                if bits[i] > 0: 
                    last = i 
            
            bits = reversed(bits[:last+1])
            return int('0b'+''.join(str(bit) for bit in bits), 2)*sign

        def xor3(total, number):
            bits = split_number_into_bits(number)
            for i in range(len(bits)):
                total[i] = (bits[i] + total[i])%3    
        result = [0 for _ in range(33)]
        for num in nums:
            xor3(result, num)
        print(result)
        return bits_into_number(result) 
start_time = time.time()
app = Solution()   
root = app.singleNumber([-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")