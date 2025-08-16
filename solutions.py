from typing import List

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


# Example usage:
sol = Solution()
s = "a#c"
t = "c"
print(f"Output: {sol.backspaceCompare(s, t)}")