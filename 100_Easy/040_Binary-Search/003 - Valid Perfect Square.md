---
Link: https://leetcode.com/problems/valid-perfect-square/description/?envType=problem-list-v2&envId=binary-search
tags:
  - Easy
  - Math
  - BinarySearch
---
## First Attempt:
*Correct Answer:*
This is the first problem I solved without AI hints or heading over to `NeetCode` to explain it:

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            m = l + ((r - l) // 2)
            sqrt = m * m
            if sqrt == num:
                return True
            elif sqrt > num:
                r = m - 1
            else:
                l = m + 1
        return False
```