---
Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Strings
  - TwoPointers
---
## 1st Attempt:
*Incorrect Answer:*
I tested many cases and all were wrong because of Index out of range exception and focus out of range as well LOL. The exception was because of the loop conditions:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        l, r, firstIndex = 0, 0, 0
        while l < len(haystack) and r < len(needle):
            if haystack[l] != needle[r]:
                l += 1  
            else:
                firstIndex = l
                while r < len(needle):
                    if haystack[l] != needle[r]:
                        break
                    l += 1
                    r += 1

                if r == (len(needle)):
                    return firstIndex
  
                r = 0
                l = firstIndex + 1
        
        return -1
```

## 2nd Attempt:
*Correct Answer:*
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        
        l, r, firstIndex = 0, 0, 0
        while l < len(haystack) and r < len(needle):
            if haystack[l] != needle[r]:
                l += 1  
            else:
                firstIndex = l
                while l < len(haystack) and r < len(needle):
                    if haystack[l] != needle[r]:
                        break
                    l += 1
                    r += 1

                if r == (len(needle)):
                    return firstIndex
  
                r = 0
                l = firstIndex + 1
        
        return -1
```

## 3rd Attempt
*Correct Answer*
I made some improvements:
```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        l = 0
        while l <= len(haystack) - len(needle):
            if haystack[l] == needle[0]:
                i = l
                r = 0
                while r < len(needle) and haystack[i] == needle[r]:
                    i += 1
                    r += 1
                if r == len(needle):
                    return l
            l += 1
            
        return -1
```