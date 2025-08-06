import math
from typing import List


# class Solution:
#     def isHappy(self, n: int) -> bool:
#         freq = { n: 0 }
#         index = 0
#         while True:
#             sum, sqrt, mod = 0, 0, 0
#             while n != 0: 
#                 mod = n % 10
#                 sqrt = mod**2
#                 sum += sqrt
#                 n = n // 10

#             if sum == 1:
#                 return True
#             if sum in freq:
#                 return False
            
#             n = sum
#             index += 1
#             freq[n] = index

#         return False

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                if nums[left] != nums[right]:
                    nums[left] = nums[right]
                    nums[right] = 0
                left += 1

if __name__ == "__main__":
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums)
    
            
