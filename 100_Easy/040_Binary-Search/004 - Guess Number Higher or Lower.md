---
Link: https://leetcode.com/problems/guess-number-higher-or-lower/description/?envType=problem-list-v2&envId=binary-search
tags:
  - BinarySearch
  - Easy
  - Interactive
---
## First Attempt:
*Correct Answer:*
I think I got the hang of binary search because I solved this with ease:
```python
class Solution:
    def guessNumber(self, n: int) -> int:
        # if n == 1:
        #     return 1
        l, r = 0, n
        while l <= r:
            m = l + ((r - l) // 2)
            if guess(m) == 0:
                return m
            if guess(m) == 1:
                l = m + 1
            if guess(m) == -1:
                r = m - 1

        return -1
```