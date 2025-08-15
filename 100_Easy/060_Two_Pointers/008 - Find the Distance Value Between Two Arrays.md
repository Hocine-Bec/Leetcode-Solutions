---
Link: https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Arrays
  - TwoPointers
  - BinarySearch
---
## 1st Attempt
*Incorrect Answer*
Made a mistake in if condition:
```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        l, r = 0, 0
        count = 0
        while l < len(arr1) and r < len(arr2):
            distance = abs(arr1[l] - arr2[r])
			
            if distance <= d:
                r = 0
                l += 1
                continue
            
            r += 1
            if r == len(arr2) - 1:
                r = 0
                l += 1
                count += 1
				
        return count
```

## 2nd Attempt
*Correct Answer*
```python
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        l, r = 0, 0
        count = 0
        while l < len(arr1) and r < len(arr2):
            distance = abs(arr1[l] - arr2[r])

            if distance <= d:
                r = 0
                l += 1
                continue
            
            r += 1
            if r == len(arr2): #fixed this
                r = 0
                l += 1
                count += 1

        return count
```

## 3rd Attempt
*Correct Answer*
Using binary search *bisect* approach:

```python
import bisect

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        count = 0
		
        for x in arr1:
            pos = bisect.bisect_left(arr2, x)
            is_valid = True
		
            if pos < len(arr2) and abs(arr2[pos] - x) <= d:
                is_valid = False
            if pos > 0 and abs(arr2[pos - 1] - x) <= d:
                is_valid = False
		
            if is_valid:
                count += 1
			
        return count
```