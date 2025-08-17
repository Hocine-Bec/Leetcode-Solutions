---
Link: https://leetcode.com/problems/backspace-string-compare/description/?envType=problem-list-v2&envId=two-pointers`
tags:
  - Easy
  - TwoPointers
  - Stack
  - Strings
---
## 1st Attempt
*Incorrect Answer*
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        seen = []
        for i in range(len(s)):
            seen.append(s[i])

        index = 0
        res = ""
        while index < len(seen) and index < len(t):
            if (seen[index] == t[index]) and (seen[index] != "#" and t[index] != "#"):
                res += t[index]
            else:
                seen.pop(index)
            index += 1
            
        for i in range(len(seen)):
            if seen[i] != res[i]:
                return False

        return True
```

## 2nd Attempt
*Incorrect Answer*
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        chars = list(s)
        for i, c in enumerate(chars, start=1):
            if c == '#':
                chars.pop(i - 2)
                chars.pop(i - 2)
        
        res1 = "".join(chars)
        
        chars = list(t)
        for i, c in enumerate(chars, start=1):
            if c == '#':
                chars.pop(i - 2)
                chars.pop(i - 2)

        res2 = "".join(chars)
        if len(res1) != len(res2):
            return False
        
        for i in range(len(res1)):
            if res1[i] != res2[i]:
                return False
        
        return True
```

## 3rd Attempt
*Incorrect Answer*

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        l, r = 0, 0
        
        while l < len(s) and r < len(t):
            if s[l] == "#" and len(sList) != 0:
                sList.pop()
            else:
                sList.append(s[l])
            
            if t[r] == "#" and len(tList) != 0:
                tList.pop()
            else:
                tList.append(t[r])

            l += 1
            r += 1
        
        if len(sList) != len(tList):
            return False
        
        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False

        return True
```

## 4th Attempt
*Correct Answer*
FINALLY!! with the help of AI
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sList = []
        tList = []
        l, r = 0, 0
        
        while l < len(s):
            if s[l] == "#":
                if len(sList) != 0:
                    sList.pop()
            else:
                sList.append(s[l])
            l += 1
        
        while r < len(t):
            if t[r] == "#":
                if len(tList) != 0:
                    tList.pop()
            else:
                tList.append(t[r])
            r += 1
        
        if len(sList) != len(tList):
            return False
        
        for i in range(len(sList)):
            if sList[i] != tList[i]:
                return False
        return True
```