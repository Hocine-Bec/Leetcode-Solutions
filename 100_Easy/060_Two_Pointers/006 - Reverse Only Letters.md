---
Link: https://leetcode.com/problems/reverse-only-letters/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Strings
  - TwoPointers
---
## 1st Attempt
*Correct Answer*
```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1 
        letters = list(s)    
        while l < r:
            if not s[l].isalpha():
                l += 1
                continue
            elif not s[r].isalpha():
                r -= 1
                continue
            
            temp = letters[l]
            letters[l] = letters[r]
            letters[r] = temp  
            
            l += 1
            r -= 1
        return "".join(letters)
```