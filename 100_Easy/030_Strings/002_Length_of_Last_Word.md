---
Link: https://leetcode.com/problems/length-of-last-word/description/
tags:
  - Easy
  - Strings
---
## Problem Statement

Given a string `s` consisting of words separated by spaces, return the length of the last word in the string. A word is a maximal substring consisting of non-space characters only.

**Example:**
```csharp
Input: s = "   fly me   to   the moon   "
Output: 4
Explanation: The last word is "moon" with a length of 4.
```

---
## Initial Thoughts

- **Split and Filter Approach**:
  - Split the string by spaces to get an array of words.
  - Filter out empty strings (resulting from multiple spaces).
  - Return the length of the last word in the filtered list.

---

## Initial Solution

```csharp
public class Solution
{
    public int LengthOfLastWord(string s)
    {
        var list = new List<string>();

        foreach (var word in s.Split(" "))
        {
            if (!string.IsNullOrEmpty(word))
                list.Add(word);
        }

        return list[list.Count - 1].Length;
    }
}
```

### Strengths:
- **Readability**: The solution is easy to understand and follows a straightforward approach.
- **Handles Multiple Spaces**: Filters out empty strings caused by multiple spaces.

### Weaknesses:
- **Space Complexity**: Uses extra space to store the list of words.
- **Inefficient for Large Inputs**: Splitting the string and filtering requires O(n) space and time, which is unnecessary for this problem.
- **Edge Case Handling**: Does not explicitly handle cases where the string contains only spaces.

---
## Mistakes

- **Unnecessary Use of List**:
  - Storing all words in a list is inefficient when we only need the last word.
- **Edge Case Oversight**:
  - The solution assumes there is at least one word in the string, which may not always be true (e.g., `s = "   "`).
- **Time and Space Complexity**:
  - The solution uses O(n) space for the list and O(n) time for splitting and filtering, which can be optimized.

---

## Optimized Solution

#### Two-Pointer Approach (Iterating from the End)

```csharp
public int LengthOfLastWord(string s)
{
	// Trim the white space at the end
	s = s.TrimEnd(); 

	//Split method return an arrays of words
    var words = s.Split(" "); 

	//Access the last element and return length
    return words[words.Length - 1].Length; 
}
```

**Steps**:
- **Trim trailing spaces**: `s.TrimEnd()` removes any trailing spaces, ensuring that the last element in the `words` array is the last word.
- **Split by spaces**: `s.Split(' ')` splits the string into an array of words.
- **Return the length of the last word**: `words[words.Length - 1].Length` directly accesses the last word and returns its length.

- **Time Complexity**: O(n)
- **Space Complexity**: O(n), due to the array created by `Split`.

---
## Edge Cases

2. **Trailing Spaces**:
   - Input: `s = "Hello World  "` → Output: `5`
3. **Leading Spaces**:
   - Input: `s = "  Hello World"` → Output: `5`
4. **Single Word**:
   - Input: `s = "Hello"` → Output: `5`

---
## Lessons Learned

- **Efficiency Matters**: Avoid unnecessary operations like splitting and storing data when the problem can be solved with a single pass.
- **Space Optimization**: Use constant space whenever possible to improve performance.

---
## Related Problems

- [LeetCode #151: Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- [LeetCode #434: Number of Segments in a String](https://leetcode.com/problems/number-of-segments-in-a-string/)
- [LeetCode #557: Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

---
## Progress Tracker

- **Status**: Solved
- **Confidence**: High (after understanding the optimized approach)
- **Revisit**: No (core concept is clear, implementation is straightforward)