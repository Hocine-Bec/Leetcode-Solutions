---
Link: https://leetcode.com/problems/move-zeroes/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Arrays
  - TwoPointers
---
## 1st Attempt:
*Correct Answer* I solved this question before but I completely forgot it and resolved it again
```python
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
```