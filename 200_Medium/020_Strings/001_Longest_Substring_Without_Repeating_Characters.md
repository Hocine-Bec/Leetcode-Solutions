---
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?source=submission-noac
tags:
  - Strings
  - Sliding-Window
  - Medium
  - HashTable
---
## Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

**Example:**
```csharp
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with a length of 3.
```

---

## Initial Thoughts

- Use a HashSet to store unique characters.
- If a duplicate is found, clear the set and start over with the current character.
- Add the current element and update the longest streak.
- Intuition: Track the current substring length and reset when a repeat occurs.

---
## Mistakes

- **Resetting the Set**:
    - Clearing the entire HashSet when a duplicate is found loses valid characters from the previous substring that could still contribute to a longer sequence.
    - Example: For "dvdf", after reaching "dvd", clearing the set and starting with the second "d" misses the optimal substring "vdf" (length 3).
- **Not Optimal**:
    - Restarting from scratch doesn’t maintain a sliding window, leading to missed opportunities for longer substrings.
    - **Time Complexity**: Still O(n), but the logic fails to capture the correct maximum length in many cases.

_Initial Code:_
```csharp
public static int LengthOfLongestSubstring(string s)
{
    if (string.IsNullOrEmpty(s))
        return 0;
        
    var set = new HashSet<char>();
    int longestStreak = 0;
    
    for (int i = 0; i < s.Length; i++)
    {
        if (!set.Contains(s[i]))
        {
            set.Add(s[i]);
        }
        else
        {
            set.Clear();
            set.Add(s[i]);
        }        
        longestStreak = Math.Max(longestStreak, set.Count);
    }
    return longestStreak;
}
```

- **Issue**: For `"abcabcbb"`, it resets at the second `"a"`, missing the chance to slide and find `"bca"` or `"cab"`. Output might be 3 but could incorrectly be lower in other cases like `"pwwkew"`.

---
## Correct Solution
#### Solution 1: Sliding Window with `HashSet`
Use a sliding window with a `HashSet` to track characters and adjust the window dynamically.

```csharp
public int LengthOfLongestSubstring(string s)
{
    if (string.IsNullOrEmpty(s)) 
		return 0;
    
    HashSet<char> set = new HashSet<char>();
    int maxLength = 0;
    int left = 0;
    
    for (int right = 0; right < s.Length; right++)
    {
        while (set.Contains(s[right]))
        {
            set.Remove(s[left]);
            left++;
        }
        set.Add(s[right]);
        maxLength = Math.Max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```
- **Steps**:
  1. Use `left` and `right` pointers to define the window.
  2. If a duplicate is found at `right`, shrink the window by removing characters from `left`.
  3. Update `maxLength` with the current window size.
- **Time**: O(n) — each character is added and removed at most once.
- **Space**: O(min(m, n)) where m is the character set size (e.g., 26 for lowercase letters).

#### Solution 2: Sliding Window with `Dictionary`
Use a dictionary to store character positions, allowing the `left` pointer to jump directly to the position after the last occurrence of a duplicate.

```csharp
public int LengthOfLongestSubstring(string s)
{
    if (string.IsNullOrEmpty(s)) return 0;
    
    var map = new Dictionary<char, int>();
    int maxLength = 0;
    int left = 0;
    
    for (int right = 0; right < s.Length; right++)
    {
        if (map.ContainsKey(s[right]))
        {
            left = Math.Max(left, map[s[right]] + 1);
        }
        map[s[right]] = right;
        maxLength = Math.Max(maxLength, right - left + 1);
    }
    
    return maxLength;
}
```
- **Steps**:
  1. Store the last position of each character in the dictionary.
  2. When a duplicate is found, move `left` to the position after the last occurrence.
  3. Update `maxLength` with the current window size.
- **Time**: O(n)
- **Space**: O(min(m, n)) where m is the character set size.
- **Note**: More efficient than HashSet for cases with many duplicates (e.g., "dvdf"), as it avoids incremental shrinking.

##### Comparison

| Approach          | Time Complexity | Space Complexity | Pros                   | Cons                        |
| ----------------- | --------------- | ---------------- | ---------------------- | --------------------------- |
| Initial (Reset)   | O(n)            | O(min(m, n))     | Simple to code         | Incorrect logic, misses max |
| Sliding (HashSet) | O(n)            | O(min(m, n))     | Intuitive, single pass | Incremental shrinking       |
| Sliding (Dict)    | O(n)            | O(min(m, n))     | Faster with duplicates | Slightly more complex       |

---
## Edge Cases

1. **Empty String**:
   - Input: `""` → Output: `0`
2. **Single Character**:
   - Input: `"a"` → Output: `1`
3. **All Same Characters**:
   - Input: `"bbbb"` → Output: `1`
4. **Duplicates with Gaps**:
   - Input: `"dvdf"` → Output: `3` (substring "vdf")
5. **No Repeats**:
   - Input: `"abcde"` → Output: `5`

---

## Lessons Learned

- **Understand the Problem**: Take time to fully grasp the requirements—resetting completely misinterprets the need for a continuous substring.
- **Sliding Window**: Learned about the sliding window technique—dynamic resizing is key for efficiency.
- **Data Structures**: `HashSet` works for presence checks, but a Dictionary is better for position-based jumps.
- **Edge Cases**: Always test empty, single-element, and repetitive inputs.

---

## Related Problems

- [LeetCode #76: Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [LeetCode #159: Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

---
## Progress Tracker

- **Status**: Not Solved
- **Confidence**: Low (after corrections, still solidifying sliding window intuition)
- **Revisit**: Yes (to reinforce sliding window with Dictionary approach)
