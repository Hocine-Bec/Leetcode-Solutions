---
Link: https://leetcode.com/problems/binary-search/description/?envType=problem-list-v2&envId=binary-search
tags:
  - Easy
  - BinarySearch
  - Arrays
---
## 1st Attempt:

*Wrong Answer*
I missed the right pointer by assigning the target value to it and cause index out of range exception:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, target
        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1

        return -1
```

## 3rd Attempt
*Wrong Answer*
Also same problem:
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:       
        l, r = 0, len(nums)
        while l < r:
            m = l + ((r - l) // 2)
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
```

## 3rd Attempt
*Correct Answer:*
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:       
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
```