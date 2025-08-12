---
Link: https://leetcode.com/problems/shortest-distance-to-a-character/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Arrays
  - Strings
  - TwoPointers
---
## 1st Attempt
*Incorrect Answer*
```python
class Solution:
	def shortestToChar(self, s: str, c: str) -> List[int]:
    prevIndx, currIndx = 0, 0
    answer = [0] * len(s) 
    j = 0
    while currIndx < len(s):
		if s[currIndx] != c:
	        currIndx += 1
	        continue
		      
		shortest = min((j - currIndx), (j - prevIndx))
		answer[j] = abs(shortest)
		if s[j] == c:
	        prevIndx = currIndx
	        currIndx += 1
		j += 1
    return answer
```

## Solution
```python
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        answer = [n] * n 
        
        last_c_pos = -n  
        for i in range(n):
            if s[i] == c:
                last_c_pos = i
            answer[i] = i - last_c_pos
        
        last_c_pos = 2 * n  
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                last_c_pos = i
            answer[i] = min(answer[i], last_c_pos - i)
        
        return answer
```