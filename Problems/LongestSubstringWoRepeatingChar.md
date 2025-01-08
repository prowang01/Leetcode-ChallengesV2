# Longest Substring Without Repeating Characters

## Description
Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## Examples

### Example 1:
**Input:**  
`s = "abcabcbb"`  
**Output:**  
`3`  
**Explanation:**  
The answer is `"abc"`, with the length of `3`.

---

### Example 2:
**Input:**  
`s = "bbbbb"`  
**Output:**  
`1`  
**Explanation:**  
The answer is `"b"`, with the length of `1`.

---

### Example 3:
**Input:**  
`s = "pwwkew"`  
**Output:**  
`3`  
**Explanation:**  
The answer is `"wke"`, with the length of `3`.  
Notice that the answer must be a substring, `"pwke"` is a subsequence and not a substring.

---

## Constraints:
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.

---

## Performance:
- **Runtime:** 15 ms  
- **Memory Usage:** 17.93 MB  

---

## Complexity:
- **Time Complexity:**  
   - **O(n)**: Each character in the string `s` is visited at most twice (once by `right` and once by `left`).
   - Adding or removing an element from the `charset` is an **O(1)** operation.

- **Space Complexity:**  
   - **O(n)**: In the worst case, all characters in `s` are unique, so the `charset` will contain up to `n` characters.

---

## Approach: Sliding Window
We use a **sliding window** with two pointers (`left` and `right`) to find the longest substring without repeating characters.

### Steps:
1. Initialize:
   - `left = 0` (start of the window).
   - `charset = set()` to store characters in the current window.
   - `maxLength = 0` to keep track of the maximum length of a substring without repeating characters.

2. Traverse the string using the `right` pointer:
   - If `s[right]` is not in `charset`, add it to the set and update `maxLength`.
   - If `s[right]` is already in `charset`, move the `left` pointer to remove characters from the window until `s[right]` is no longer in the set. Then, add `s[right]` to the set.

3. Return `maxLength` at the end.

---

## Code:
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charset = set()
        maxLength = 0
        
        for right in range(len(s)):  
            if s[right] not in charset:
                charset.add(s[right])
                maxLength = max(maxLength, right - left + 1)  
            else:
                while s[right] in charset:
                    charset.remove(s[left])
                    left += 1
                charset.add(s[right])  
        return maxLength
