---
Link: https://leetcode.com/problems/valid-parentheses/description/
tags:
  - Stack
  - Strings
  - Easy
---
### **1. Problem Statement**

Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
An input string is valid if:
2. Open brackets must be closed by the same type of brackets.
3. Open brackets must be closed in the correct order.
4. Every close bracket has a corresponding open bracket of the same type.	

```json
	Example 1:
		Input: s = "()[]{}"
		Output: true
	Example 2:
		Input: s = "([{}])"
		Output: false
```

---
### **2. Initial Thoughts**

The approach I used when solving this problem was a combination of `Stack` and `StringBuilder`.
5. Iterate through the string.
6. Use `Stack` to store the closing brackets `)`, `]`, and `}`.
7. Use `StringBuilder` to store the opening brackets `(`, `[`, and `{`.
8. Then Iterate through `StringBuilder` and Check it matches the top of stack:
	-  If it matches, pop from the stack.
9. Lastly, Check if Stack is Empty and return the result.

**Attempted Solution Code:**
```csharp
 public bool IsValid(string s)
    {
        var stack = new Stack<char>();
        var st = new StringBuilder();

        foreach (char c in s)
        {
            if (c == ')' || c == ']' || c == '}')
            {
                stack.Push(c);
            }
            else
            {
                st.Append(c);
            }
        }

        if (st.Length > stack.Count)
            return false;

        for (int i = 0; i < st.Length; i++)
        {
            if (st[i] == '(' && stack.Peek() == ')')
            {
                stack.Pop();
            }

            if (st[i] == '[' && stack.Peek() == ']')
            {
                stack.Pop();
            }

            if (st[i] == '{' && stack.Peek() == '}')
            {
                stack.Pop();
            }
        }
        return (stack.Count == 0) ? true : false;
    }
```

---
### **3. Mistakes**
 
- This Solution is inefficient because I'm not checking the open and it's closing brackets instead I'm tracking `Stack` status which could be wrong.
- if I gave it this string: `([{]})`, it will give `True` where it should be `False`. 

---
### **4. Correct Solution**

- `StringBuilder` is not necessary for this problem and it can be solve using `Stack` only.
- Use `Stack` to store the opening brackets instead of the closing brackets
- Using only one loop, we can check if it's an opening bracket we add to the stack if not, we then pop an element from the stack and compare it with the char we're processing to see if they match or not.

**Correct Solution Code:**
```csharp
public bool IsValid(string s)
{
    var stack = new Stack<char>();

    foreach (char c in s)
    {
        if (c == '(' || c == '[' || c == '{')
        {
            // Push opening brackets onto the stack
            stack.Push(c);
        }
        else
        {
            // If the stack is empty, there's no matching opening bracket
            if (stack.Count == 0)
                return false;

            // Check if the closing bracket matches the top of the stack
            char top = stack.Pop();
            if ((c == ')' && top != '(') ||
                (c == ']' && top != '[') ||
                (c == '}' && top != '{'))
            {
                return false;
            }
        }
    }

    // If the stack is empty, all brackets were matched correctly
    return stack.Count == 0;
}
```

- **Time Complexity**: **O(n)** – Each character is processed once.
- **Space Complexity**: **O(n)** – The stack can grow up to the size of the input string.

---
### **5. Edge Cases**

- Empty string
- Unmatched brackets (e.g., `"([)]"`).

---

### **7. What I learned**

- You shouldn't start every problem from the result because sometimes it will take on the wrong path (Choosing closed brackets first instead of open brackets). 

---

### **8. Related Problems**

- [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/)
- [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

---
### **9. Progress Tracker**

- **Status**: I didn't solve it
- **Confidence Level**: Medium
- **Revisit**: Yes

---

>[!Related Concepts]
>- [[026_Stacks]]
