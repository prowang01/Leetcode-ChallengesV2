# Approach : Using a stack, just putting the opening brackets, and match the closing brackets
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

# Runtime : 0 ms / Memory : 18.09 MB 
# Complexity : O(n) Time and O(n) Space
'''
Time : Browsing all the characters in s, so O(n), append and pop operations are O(1).
Space : O(n) in the worst case, just about stocking the opening brackets of s.
'''

# NB : can't do this without stack. A method exists, but strings are immutable in Python, so unsuitable.