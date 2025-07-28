---
Link: https://leetcode.com/problems/sqrtx/description/
tags:
  - BinarySearch
  - Easy
---
## First Attempt:
*Incorrect Answer*
I tried to solve it using Binary search directly but one problem I faced was that I didn't know how to exist the loop + I had some logical errors.
```csharp
public class Solution {
    public int MySqrt(int x)
    {
        int low = 1, high = x;
        while (low < high)
        {
            int mid = low + (high - low) / 2;
            long squareRoot = (long)(mid * mid);
            if (x < squareRoot)
                high = mid - 1;
            else
                low = mid ;
        }
        return ans;
    }
}
```

## Second Attempt:
*Correct Answer*

I watched `NeetCode` video about the problem and realized my mistake.
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        res = 0
        while l <= h:
            m = l + ((h - l) // 2)
            if (m * m) > x:
                h = m - 1
            elif (m * m) < x:
                l = m + 1
                res = m
            else:
                return m
        return res
```