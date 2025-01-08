# Approach : convert the integer into a string, and compare the string and its reverse
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        return False
        
# Runtime : 5 ms / Memory : 17.85 MB
# Complexity : O(n) Time and O(n) Space
'''
- Converting n digits / characters, and reversing n characters so O(n)
- Creating the string representation of x and its reversed version both take O(n) space
'''



# Approach : comparing the reversed half of x, instead of reversing everything
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x!=0 and x%10 == 0):
            return False
        else:
            reversed_num = 0

        while x > reversed_num:
            reversed_num = reversed_num*10 + x%10 # Put the last number of x and shift the previous digit to the left
            x //= 10
        return x == reversed_num or x == reversed_num//10 # Even and odd number cases, 2nd ignore the middle digit.

# Runtime : 8 ms / Memory : 17.80 MB

'''
Time and Space Complexity:
The loop runs while x > reversed_num. In each iteration:
x is divided by 10 (x //= 10), effectively reducing its number of digits by 1.
Total Time Complexity: O(log₁₀(x)).

The algorithm does not use any extra space that grows with the size of the input. It only uses a few integer variables (reversed_num, x), so the space complexity is O(1) (constant space).
'''