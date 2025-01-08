# Approach : Two Sliding Window to find the window with the longest substring.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        charset = set()
        maxLength = 0
        for right in range (len(s)): # right need to be an integer, for indexes it's important.
            if s[right] not in charset:
                charset.add(s[right])
                maxLength = max(maxLength, right - left + 1) # Update the longest substring, between the max / new one.
            else:
                while s[right] in charset:  # While the repeating character is still in the set
                    charset.remove(s[left])   # Remove from the left
                    left += 1
                charset.add(s[right])
        return maxLength

# Runtime : 15 ms / Memory : 17.93 MB
# Complexity : O(n) Time and Space

'''
Time : Iterating through the string with n characters
+ deleting characters : n characters at the worst case so everything is linear.
Space : for n unique characters in the string, we have O(n)
''' 

# Same Approach but using hashmap / dictionary
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        chardict = {}
        for right in range (len(s)):
            if s[right] not in chardict or chardict[s[right]] < left: #  its index is less than left 
            # means that a repeated character that is on the left side on the window will be ignored
                chardict[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = chardict[s[right]] + 1
                chardict[s[right]] = right  # to update the new position of right if occurrences appeared
        return maxLength


# Runtime : 15 ms / Memory : 17.85 MB
# Complexity : O(n) Time and O(n) Space
'''
Time : iterate the string with right
The hashmap gives some O(1) complexity,
and left is moved if needed, but can go to O(n)

Space : The hashmap can have up to n unique characters, so O(n).
'''