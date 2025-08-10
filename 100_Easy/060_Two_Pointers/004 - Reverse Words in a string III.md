---
Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/description/?envType=problem-list-v2&envId=two-pointers
tags:
  - Easy
  - Strings
  - TwoPointers
---
## 1st Attempt
*Correct Answer*
The solution is straight-forward, I only had an issue with the language itself.
```python
class Solution:
    def reverseWords(self, s: str) -> str:
      words = s.split(" ")  
      for i in range(len(words)):
        chars = list(words[i])
        left, right = 0, len(chars) - 1

        while left < right:
          chars[left], chars[right] = chars[right], chars[left]
          left += 1
          right -= 1

        words[i] = "".join(chars)

      return " ".join(words)
```

## 2nd Attempt
*Correct Answer*
Shorter version:
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")  # split on spaces
        reversed_words = [word[::-1] for word in words]  # reverse each word
        return " ".join(reversed_words)
```