from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         if len(nums) <= 1:
#             return nums[0]
        
#         currSum = 0
#         for i in range(k):
#             currSum += nums[i]
            
#         avg = currSum / k
#         l, r = 0, k            
#         while r < len(nums):
#             currSum = currSum - nums[l] + nums[r]
#             currAvg = currSum / k
#             avg = max(currAvg, avg)
#             l += 1
#             r += 1

#         return avg

# Clean up version of the code
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum
        
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        
        return maxSum / k
    

# Example usage:
sol = Solution()
nums = [7,4,5,8,8,3,9,8,7,6]
k = 7
print(f"Output: {sol.findMaxAverage(nums, k)}")