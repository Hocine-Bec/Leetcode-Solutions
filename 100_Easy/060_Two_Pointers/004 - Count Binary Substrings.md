---
Link: https://leetcode.com/problems/count-binary-substrings/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - TwoPointers
  - Strings
---
## 1st Attempt
*Incorrect Answer*
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
      groups = []
      l, r = 0, 0  
      count = 0 
      while l < len(s) and r < len(s):
        if s[l] == s[r]:
          count +=1
          r += 1
        else:
          groups.append(count)
          count = 0
          l = r

      l, r, res = 0, 1, 0
      while r < len(groups):
        res += min(groups[l], groups[r])
        l += 1
        r += 1

      return res
```

## 2nd Attempt
*Correct Answer*
```python
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        l, r = 0, 0  
        count = 0 
        while l < len(s) and r < len(s):
            if s[l] == s[r]:
                count += 1
                r += 1
            else:
                groups.append(count)
                count = 1 
                l = r
                r += 1  
        groups.append(count)
        l, r, res = 0, 1, 0
        while r < len(groups):
            res += min(groups[l], groups[r])
            l += 1
            r += 1
			
		return res
```