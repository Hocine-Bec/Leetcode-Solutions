---
tags:
  - Arrays
  - Easy
  - HashTable
Link: https://leetcode.com/problems/intersection-of-two-arrays/description/?envType=problem-list-v2&envId=binary-search
---
## Solution
*Correct Answer:*

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniqSet = set(nums1)
        res = []
        for n in nums2:
            if n in uniqSet:
                res.append(n)
                uniqSet.remove(n)
            
        return res; 
```