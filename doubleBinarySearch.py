from typing import List
import time
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        return [self.searchBinaryLeft(nums, target), self.searchBinaryRight(nums, target)]
    def searchBinaryRight(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        if (nums[right] == target):
            return right
        while (left <= right):
            mid = left + (right - left)//2
            if (nums[mid] == target and nums[mid+1] > target):
                return mid
            if (nums[mid] > target):
                right = mid - 1
            else:
                left = mid + 1 
        return -1
    def searchBinaryLeft(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums)-1
        if (nums[left] == target):
            return left
        while (left <= right):
            mid = left + (right - left)//2
            if (nums[mid] == target and nums[mid-1] < target):
                return mid
            if (nums[mid] >= target):
                right = mid - 1
            else:
                left = mid + 1 
        return -1

t = time.time()
nums = [7, 8, 8]
print(Solution().searchRange(nums, 8))
print(f"{(time.time() - t)}")