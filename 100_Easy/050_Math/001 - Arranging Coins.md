---
Link: https://leetcode.com/problems/arranging-coins/submissions/1720340735/?envType=problem-list-v2&envId=binary-search
tags:
  - Easy
  - Math
---
This was tagged as a binary search problem but I didn't use it
## First Attempt:
*Correct Answer*
I had some difficulty understanding the problem at first. I built a correct algorithm but returned the false variable instead (rookie mistake haha):
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, res = 1, 0
        while i <= n:
            n = n - i
            res = i # here I returned n instead of i 
            i += 1
        return res
```

## Second Attempt:
After the first solution, I noticed how easy it was and thought if there was a mathimatical equition to solve this. So I had a nice chat with `ChatGbt` and here it is:
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8 * n + 1) - 1) // 2)
```