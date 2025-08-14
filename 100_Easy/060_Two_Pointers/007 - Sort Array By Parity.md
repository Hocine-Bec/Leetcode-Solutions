---
Link: https://leetcode.com/problems/sort-array-by-parity/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Arrays
  - TwoPointers
---
## 1st Attempt
*Correct Answer*
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1     
        while l < r:
            if nums[l] % 2 == 0:
                l += 1
                continue
            elif nums[r] % 2 != 0:
                r -= 1
                continue
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp  
            
            l += 1
            r -= 1
        return nums
```

## 2nd Attempt
*Correct Answer*
Read about using `bitwise` operation instead of division which is faster in terms of performance
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1     
        while l < r:
            if (nums[l] & 0x1) == 0:
                l += 1
                continue
            elif (nums[r] & 0x1) != 0:
                r -= 1
                continue
            
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums
```