---
Link: https://leetcode.com/problems/reverse-string-ii/description/
tags:
  - Easy
  - Strings
  - TwoPointers
---
I didn't solve this problem at all and I still have some trouble understanding even after seeing the solution. 

## My Attempt
*Incorrect Answer*
I did solve 2 conditions: Reverse all and reverse the first 2k blocks but missed the last condition where I reverse the 1st 2k blocks and leave the rest.

```C#
public class Solution {
    public string ReverseStr(string s, int k)
    {
        if (string.IsNullOrEmpty(s))
            return "";
        
        char[] arr = s.ToCharArray();
        int left = 0, right = s.Length - 1;
        char temp;
        if (s.Length <= k)
        {
            while (right > left)
            {
                temp = arr[left];
                arr[left] = arr[right];
                arr[right] = temp;
                left++;
                right--;
            }
            return new string(arr);
        }
        
        while (right < arr.Length)
        {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;

            left += k * 2;
            right += k * 2;
        }
         return new string(arr);
    }
}
```
## 1st Attempt:
*Correct Answer*
```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        arr = list(s)
        for i in range(0, len(arr), 2 * k):
            l = i
            m = i+k-1
            if m >= len(arr):
                m = len(arr) - 1
            while l < m:
                arr[l], arr[m] = arr[m], arr[l]
                l += 1
                m -= 1
        return ''.join(arr)
```
## 2nd Attempt:
*Correct Answer*
```C#
public class Solution {
    public string ReverseStr(string s, int k) {
        if (string.IsNullOrEmpty(s))
            return "";

        char[] arr = s.ToCharArray();
        for (int start = 0; start < s.Length; start += 2 * k) {
            int i = start;
            int j = Math.Min(start + k - 1, s.Length - 1);
            
            while (i < j) {
                char temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
        return new string(arr);
    }
}
```

The solutions are similar in some aspects. In short, the problem have 3 conditions:
1. Reverse the first `k` characters for every `2k` characters in the string. 
2. If fewer than `k` characters remain, reverse all of them.
3. If between `k` and `2k` characters remain, reverse the first `k` and leave the rest.
w