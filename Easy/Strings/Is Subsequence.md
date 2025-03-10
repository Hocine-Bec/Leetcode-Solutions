---
Link: https://leetcode.com/problems/is-subsequence/description/
tags:
  - Strings
  - TwoPointers
  - DynamicProgramming
  - Easy
---
## Problem Statement

Given two strings `s` and `t`, check if `s` is a subsequence of `t`. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

**Example:**
```csharp
Input: s = "abc", t = "ahbgdc"
Output: true
Explanation: "abc" is a subsequence of "ahbgdc" because the characters 'a', 'b', and 'c' appear in order within "ahbgdc".
```

---

## Initial Thoughts

- **Two-Pointer Approach**:
	- Use two pointers, one for `s` (`p1`) and one for `t` (`p2`).
	- Traverse `t` with `p2` and check if the current character matches `s[p1]`.
	- If a match is found, set `IsSubs` to `true` and move `p1` forward.
	- If `p1` reaches the end of `s`, `s` is a subsequence of `t`.
	- If we can reach the end of string `s`, it means `s` is a subsequence of `t`.

---
## Mistakes

- **Incorrect Handling of Edge Cases**:
    - Returning `false` for empty strings is incorrect. An empty string is a valid subsequence of any string.
- **Single Character Handling**:
    - Using `Contains` for a single-character `s` works, but the condition to check is unnecessary for the general algorithm.
- **Return Condition Logic**:
    - The function checks `p1 == s.Length - 1` to determine if we found a match, but this checks only if we're at the last character, not if we've processed all characters.
- **Early Return Issue**:
    - The function returns `IsSubs` when `p1 == s.Length - 1`, but this might be premature if the last character hasn't been matched yet.
- **Incorrect Pointer Logic**:
	  - Initially, I forgot to reset the `IsSubs` flag when no match was found, leading to incorrect results.

*Initial Code:*
```csharp
public bool IsSubsequence(string s, string t) {
    if (string.IsNullOrEmpty(s) || string.IsNullOrEmpty(t))
        return false;

    if (s.Length > t.Length)
        return false;

    if (s.Length == 1)
    {
        return t.Contains(s[0]);
    }
    
    bool IsSubs = false;

    for (int p1 = 0, p2 = 0; p2 < t.Length; p2++)
    {
        if (p1 == s.Length - 1)
            return IsSubs;
        
        if (s[p1] == t[p2])
        {
            IsSubs = true;
            p1++;
        }
    }

    return IsSubs;
}
```
- **Issue**: The `IsSubs` flag is not reset properly, and the loop terminates early without fully checking the subsequence.

---

## Correct Solution

#### Two-Pointer Approach

```csharp
public bool IsSubsequence(string s, string t) {
    if (string.IsNullOrEmpty(s)) 
        return true; // Empty string is always a subsequence
    if (string.IsNullOrEmpty(t)) 
        return false; // Non-empty s cannot be a subsequence of empty t
    if (s.Length > t.Length) 
        return false; // s cannot be longer than t

    int p1 = 0, p2 = 0;

    while (p1 < s.Length && p2 < t.Length)
    {
        if (s[p1] == t[p2])
        {
            p1++; // Move pointer in s
        }
        p2++; // Always move pointer in t
    }

    return p1 == s.Length; // If p1 reached the end, s is a subsequence
}
```
- **Steps**:
	  1. Handle edge cases (empty strings, `s` longer than `t`).
	  2. Use two pointers, `p1` for `s` and `p2` for `t`.
	  3. Traverse `t` with `p2` and check for matches with `s[p1]`.
	  4. If a match is found, move `p1` forward.
	  5. If `p1` reaches the end of `s`, return `true`; otherwise, return `false`.

- **Time Complexity**: O(n), where `n` is the length of `t`.
- **Space Complexity**: O(1), no extra space is used.

#### Recursion Approach

```C#
  public bool IsSubsequence(string s, string t)
  {
      return IsSubsequence(s,t , 0, 0);
  }

  public bool IsSubsequence(string s, string t, int p1, int p2)
  {
      if (p1 == s.Length)
      {
          return true; // All characters of s are matched
      }

      if (p2 == t.Length)
      {
          return false; // Reached end of t without matching all of s
      }

      if (s[p1] == t[p2])
      {
          return IsSubsequence(s, t, p1 + 1, p2 + 1);  //Increment both p1 and p2
      }
      else
      {
          return IsSubsequence(s, t, p1, p2 + 1); //Increment only p2
      }
  }
```

- **Time Complexity**: O(n), where `n` is the length of `t`.
- **Space Complexity**: O(1), no extra space is used.

---

## Edge Cases

1. **Empty `s`**:
   - Input: `s = ""`, `t = "ahbgdc"` → Output: `true`
2. **Empty `t`**:
   - Input: `s = "abc"`, `t = ""` → Output: `false`
3. **Single Character `s`**:
   - Input: `s = "a"`, `t = "ahbgdc"` → Output: `true`
4. **No Subsequence**:
   - Input: `s = "axc"`, `t = "ahbgdc"` → Output: `false`
5. **Full Subsequence**:
   - Input: `s = "abc"`, `t = "defabc"` → Output: `true`

---
## Lessons Learned

- **Edge Case Handling**: Properly handle edge cases.
- **Two-Pointer Technique**: Learned how 2 pointers are used to efficiently solve problems.
- **Flag Variables**: Be careful with flag variables; they can cause subtle logic errors.
- **Early Termination**: Ensure the loop fully traverses `t` before concluding.
---

## Related Problems

- [LeetCode #1143: Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence/)
- [LeetCode #524: Longest Word in Dictionary through Deleting](https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/)
- [LeetCode #792: Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences/)

---

## Progress Tracker

- **Status**: Solved
- **Confidence**: High (after corrections and understanding the two-pointer approach)
- **Revisit**: No (core concept is clear, implementation is straightforward)
