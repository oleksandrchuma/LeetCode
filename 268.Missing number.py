from typing import List 
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)+1
        if n%2 == 1:
            nums += [n]
            n += 1
        for num in nums:
            s = (s + num + 1)%(n+1) 
        return n - s
app = Solution()
print(app.missingNumber([0]))

