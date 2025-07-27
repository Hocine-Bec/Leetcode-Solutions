---
Link: https://leetcode.com/problems/longest-common-prefix/description/
tags:
  - Easy
  - Strings
---
## Problem Statement

Given an array of strings `strs`, write a function to find the longest common prefix string amongst all the strings. If there is no common prefix, return an empty string `""`.

**Example:**
```csharp
Input: strs = ["flower", "flow", "flight"]
Output: "fl"
Explanation: "fl" is the longest prefix common to all three strings.
```

---

## Initial Thoughts

- **Character-by-Character Comparison**:
  - Iterate through characters of one string and compare with the same positions in others.
  - Build the prefix by adding matching characters.
- **Pairwise Approach**:
  - Compare strings in pairs and keep reducing the prefix.
  - Intuition: Eventually converge on the common prefix across all strings.

---

## Mistakes

- *Initial Code*:
```csharp
public string LongestCommonPrefix(string[] strs)
{
    if(strs == null || strs[0] == "") {
        return "";
    }   
    
    if(strs.Length == 1) {
        return strs[0];
    }

    string result = "";

    for (int i = 1, j = 0; i < strs.Length - 1; i++)
    {
        result = "";
        string word = strs[j];
        int index = 0;
        
        foreach (var c in strs[i])
        {
            if(word[index] == c)
                result += c;
            else
                break;

            index++;
        }
    }
    return result;
}
```

- **Issues**:
  1. **Incomplete Null Check**:
     - Only checked `strs[0] == ""`, but `strs == null` could still throw an exception before that check.
  2. **Loop Range Error**:
     - Loop from `i = 1` to `strs.Length - 2` (`< Length - 1`) skipped the last string and didn’t compare all elements.
     - For `["flower", "flow", "flight"]`, it only compared "flow" with "flower", ignoring "flight".
  3. **Resetting Result**:
     - `result = ""` inside the loop erased previous progress each iteration.
  4. **Pairwise Logic Flaw**:
     - Compared `strs[0]` with each subsequent string independently, but didn’t ensure the prefix was common to *all* strings.
     - Result reflected only the last comparison (e.g., "flow" vs "flight" → "fl"), ignoring earlier strings.
  5. **Index Out of Bounds Risk**:
     - No length check on `word[index]`; if `strs[i]` is longer than `word`, it throws an exception.


- **Behavioral Example**:
  - Input: `["flower", "flow", "flight"]`
  - First iteration: "flower" vs "flow" → "flow"
  - Second iteration: "flower" vs "flight" → "fl"
  - Output: "fl" (correct by chance, but not guaranteed for all cases).

---
## Correct Solution

#### Approach 1: Vertical Scanning (Character-by-Character)
```csharp
public string LongestCommonPrefix(string[] strs)
{
    if (strs == null || strs.Length == 0 || strs[0] == "")
        return "";
    
    var result = new StringBuilder();
    int minLength = strs.Min(s => s.Length);
    
    for (int i = 0; i < minLength; i++)
    {
        char current = strs[0][i];
        for (int j = 1; j < strs.Length; j++)
        {
            if (strs[j][i] != current)
                return result.ToString();
        }
        result.Append(current);
    }
    
    return result.ToString();
}
```
- **Steps**:
  1. Find the shortest string length to avoid out-of-bounds errors.
  2. Compare characters at each position across all strings.
  3. Stop at the first mismatch and return the prefix built so far.
- **Time**: O(S), where S is the sum of all characters in all strings.
- **Space**: O(1) or O(n) if counting the StringBuilder.

#### Approach 2: Horizontal Scanning (Prefix Reduction)
```csharp
public string LongestCommonPrefix(string[] strs)
{
    if (strs == null || strs.Length == 0 || strs[0] == "")
        return "";
    
    string prefix = strs[0];
    
    for (int i = 1; i < strs.Length; i++)
    {
        while (!strs[i].StartsWith(prefix))
        {
            prefix = prefix.Substring(0, prefix.Length - 1);
            if (prefix.Length == 0)
                return "";
        }
    }
    
    return prefix;
}
```
- **Steps**:
  1. Start with the first string as the prefix.
  2. Compare with each subsequent string, trimming the prefix until it matches.
  3. Return the final prefix or "" if none exists.
- **Time**: O(S), where S is the sum of all characters in all strings.
- **Space**: O(1) (excluding input).

##### Comparison

| Approach        | Time Complexity | Space Complexity | Pros                     | Cons                     |
|-----------------|-----------------|------------------|--------------------------|--------------------------|
| Vertical Scan   | O(S)            | O(1) or O(n)     | Intuitive, early exit    | More comparisons         |
| Horizontal Scan | O(S)            | O(1)             | Fewer comparisons        | String manipulation cost |

---

## Edge Cases

1. **Empty Array**:
   - Input: `[]` → Output: `""`
2. **Single String**:
   - Input: `["hello"]` → Output: `"hello"`
3. **No Common Prefix**:
   - Input: `["dog", "cat", "bird"]` → Output: `""`
4. **All Same String**:
   - Input: `["test", "test", "test"]` → Output: `"test"`
5. **Mixed Lengths**:
   - Input: `["interspecies", "interstate", "internet"]` → Output: `"inters"`

---

## Lessons Learned

- **Scope of Comparison**: pairwise approach missed the "all strings" requirement—ensure every element contributes to the result.
- **Initialization Placement**: Resetting `result` inside the loop lost progress; initialize accumulators outside loops unless the problem demands otherwise.
- **Boundary Awareness**: Unchecked string lengths led to potential crashes—always validate indices or use safe constructs (e.g., `Min` length).
- **Problem Constraints**: The goal was a prefix, not just pairwise matches; align your logic with the full problem definition.
- **Debugging Insight**: Test with small cases (e.g., ["a", "b"]) to catch logic flaws early.

---

## Related Problems

- [LeetCode #13: Roman to Integer](https://leetcode.com/problems/roman-to-integer/)
- [LeetCode #125: Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

---
## Progress Tracker

- **Status**: Solved (with help)
- **Confidence**: Medium (understand the fix, but need practice with string iteration)
- **Revisit**: Yes (to master prefix-building intuition and edge cases)
