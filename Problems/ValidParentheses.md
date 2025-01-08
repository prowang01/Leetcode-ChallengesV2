# Valid Parentheses

## Description
Given a string `s` containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['`, and `']'`, determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

---

## Examples

### Example 1:
**Input:**  
`s = "()"`  
**Output:**  
`true`  

---

### Example 2:
**Input:**  
`s = "()[]{}"`  
**Output:**  
`true`  

---

### Example 3:
**Input:**  
`s = "(]"`  
**Output:**  
`false`  

---

### Example 4:
**Input:**  
`s = "([)]"`  
**Output:**  
`false`  

---

### Example 5:
**Input:**  
`s = "{[]}"`  
**Output:**  
`true`  

---

## Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of parentheses only `'(){}[]'`.

---

## Performance:
- **Runtime:** 0 ms  
- **Memory Usage:** 18.09 MB  

---

## Complexity:
- **Time Complexity:**  
   - `O(n)` where `n` is the length of `s`.  
   - Traversing all characters in `s` once. Append and pop operations are `O(1)`.

- **Space Complexity:**  
   - `O(n)` in the worst case, if all characters are opening brackets and need to be stored.

---

## Approach: Using a Stack
We use a stack to store the opening brackets and match them with the closing brackets.

### Steps:
1. Traverse each character in the string `s`.
2. If the character is an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
3. If the character is a closing bracket (`')'`, `'}'`, `']'`):
   - Check if the stack is empty. If yes, return `false`.
   - Otherwise, pop the top element from the stack and check if it matches the closing bracket.
   - If it doesn’t match, return `false`.
4. At the end of the traversal, check if the stack is empty. If yes, the string is valid.

---

## Code:
```python
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        for bracket in s:
            if bracket == '(' or bracket == '{' or bracket == '[':
                temp.append(bracket)
            elif bracket == ']' or bracket == '}' or bracket == ')':
                if not temp : 
                    return False
                
                top = temp.pop()
                if (top == '(' and bracket != ')') or \
                   (top == '[' and bracket != ']') or \
                   (top == '{' and bracket != '}'):
                   return False
        return len(temp) == 0

        
