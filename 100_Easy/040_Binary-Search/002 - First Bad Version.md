---
Link: https://leetcode.com/problems/first-bad-version/description/?envType=problem-list-v2&envId=binary-search
tags:
  - Easy
  - BinarySearch
  - Interactive
---
## First Attempt
*Incorrect Answer*
I did a brute force solution but the time limit exceed:
```C#
/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl 
{
    public int FirstBadVersion(int n)
    {
        for (int i = 0; i <= n; i++)
        {   
            if (IsBadVersion(i))
            return i;
        }
        return -1;
    }
}
```

## Second Attempt:
*Incorrect Answer*
The problem with this is that I'm assuming that the first number to match is the first bad version:

```C#
/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */

public class Solution : VersionControl {

    public int FirstBadVersion(int n)
    {
        int left = 0, right = n;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;
            if (IsBadVersion(mid))
                return mid;
            
            if (n < mid)
                right = mid;
            else
                left = mid + 1;
        }
        
        return -1;
    }
}
```

## Third Attempt:
*Correct Answer*
Had to look it up in YouTube to understand why it was wrong.
```C#
/* The isBadVersion API is defined in the parent class VersionControl.
      bool IsBadVersion(int version); */
public class Solution {

    public int FirstBadVersion(int n)
    {
        int left = 0, right = n;
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (Program.IsBadVersion(mid))
                right = mid;
            else
                left = mid + 1;
        }
            
        return right;
    }
}
```

Python implementation: i'm doing this because I want to get familiar with python syntex without wasting time studying a course about it.
```python
class Solution:    
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            m = l + ((r - l)//2)
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l
```