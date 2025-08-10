import math
from typing import List


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


if __name__ == "__main__":
    sol = Solution()
    s = "Mr Ding"
    print(sol.reverseWords(s))
    
