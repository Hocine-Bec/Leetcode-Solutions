---
Link: https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=problem-list-v2&envId=sliding-window
tags:
  - Arrays
  - Easy
  - Sliding-Window
---
## 1st Attempt
*Incorrect Answer*
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
    if len(nums) <= 1:
	    return nums[0]
	
      currSum = 0
    for i in range(k):
        currSum += nums[i]
            
    avg = currSum / 4
    l = 0            
    while k < len(nums):
        currSum = (currSum - nums[l] + nums[k]) / 4
        avg = max(currSum, avg)
        l += 1
        k += 1
	
      return avg
```

## 2nd Attempt
*Correct Answer*
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= 1:
            return nums[0]
        
        currSum = 0
        for i in range(k):
            currSum += nums[i]
            
        avg = currSum / k
        l, r = 0, k            
        while r < len(nums):
            currSum = currSum - nums[l] + nums[r]
            currAvg = currSum / k
            avg = max(currAvg, avg)
            l += 1
            r += 1

        return avg
```

## 3rd Attempt
*Correct Answer*
```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum
        
        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        
        return maxSum / k
```
