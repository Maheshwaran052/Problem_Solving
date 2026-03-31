""" Algorithm

Initialize a set to store characters in the current window.

Use two pointers: left and right to represent the sliding window.

Traverse the string using right.

If the current character already exists in the set:

Shrink the window by removing characters from the left.

Move left forward until the duplicate is removed.

Add the current character to the set.

Update the maximum length of the window (right - left + 1).

Continue until the string ends.

Return max_length.
 """
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stringSet = set()
        n = len(s)
        left = 0
        max_length = 0

        for right in range(n):
            while(s[right] in stringSet):
                stringSet.remove(s[left])
                left+=1
            stringSet.add(s[right])
            max_length = max(max_length,right-left+1)
        return max_length