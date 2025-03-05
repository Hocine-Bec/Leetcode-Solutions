---
Link: https://leetcode.com/problems/merge-strings-alternately/
tags:
  - "#TwoPointers"
  - "#Strings"
  - Easy
---
#### **Problem Statement**

- **Title**: 
	Merge Strings Alternately

- **Description**:  
    You are given two strings, `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer than the other, append the additional letters to the end of the merged string.
    

---

#### **Approach**

1. Use two pointers, `p1` and `p2`, to track the current position in `word1` and `word2`.
2. Append characters alternately from `word1` and `word2` to the result.
3. If one pointer reaches the end of its string, append the remaining characters from the other string.

---

#### **Solution Code**
```csharp
public static string MergeAlternately(string word1, string word2)
{
    var merged = new StringBuilder();
    int p1 = 0, p2 = 0; // Two pointers
    int len1 = word1.Length, len2 = word2.Length;

    // Traverse both strings using the pointers
    while (p1 < len1 || p2 < len2)
    {
        if (p1 < len1)
        {
            merged.Append(word1[p1]);
            p1++;
        }

        if (p2 < len2)
        {
            merged.Append(word2[p2]);
            p2++;
        }
    }

    return merged.ToString();
}
```

---

#### **Explanation**

1. **Two Pointers**:
    - `p1` tracks the current index in `word1`.
    - `p2` tracks the current index in `word2`.
    
2. **Loop**:
    - The loop continues until both pointers reach the end of their respective strings.
    - Characters are appended alternately from `word1` and `word2`.
    
3. **Remaining Characters**:
    - If one string is longer, the remaining characters are appended to the result.

---

#### **Time and Space Complexity**

- **Time Complexity**: **O(n + m)**, where `n` and `m` are the lengths of `word1` and `word2`.
    - Each character is processed exactly once.
- **Space Complexity**: **O(n + m)** for the `StringBuilder` to store the result.

---

#### **Edge Cases**

1. **One String is Empty**:
    - If `word1` is empty, the result is `word2`.
    - If `word2` is empty, the result is `word1`.
    
2. **Strings of Equal Length**:
    - The result alternates characters perfectly.
    
3. **Strings of Different Lengths**:
    - The longer string's remaining characters are appended at the end.

---

#### **Mistakes and Debugging**

1. **Incorrect Pointer Update**:
    - Initially, I forgot to increment `p1` and `p2` after appending characters, causing an infinite loop.
    - Fixed by adding `p1++` and `p2++` inside the loop.
    
2. **Handling Unequal Lengths**:
    - Missed appending the remaining characters of the longer string.
    - Fixed by adding checks for `p1 < len1` and `p2 < len2`.

---

#### **Optimizations**

- The solution is already optimal with **O(n + m)** time and space complexity.
- No further optimizations are needed.

---

#### **Alternative Solutions**

1. **Using Substring (Inefficient)**:
    - Repeatedly using `Substring(1)` to remove the first character of the strings.
    - Time Complexity: **O(n^2)** due to repeated string copying.
    - Not recommended for large inputs.

---

#### **Related Problems**

- [Merge Two Sorted Lists]([Merge Two Sorted Lists - LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/description/))
- [Add Strings]([Add Strings - LeetCode](https://leetcode.com/problems/add-strings/description/))
- [Longest Common Prefix]([Longest Common Prefix - LeetCode](https://leetcode.com/problems/longest-common-prefix/description/))
