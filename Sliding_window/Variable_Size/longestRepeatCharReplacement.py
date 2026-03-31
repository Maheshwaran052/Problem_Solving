""" Update max frequency of element in window.

Check if window is valid (window_size - maxFreq <= k).

If invalid → shrink window (move left) until valid.

Update max length of valid window.

Expand window by moving right. """

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        maxFreq = 0
        maxLength = 0

        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1

            maxFreq = max(maxFreq, hashMap[s[right]])

            while (right - left + 1) - maxFreq > k:
                hashMap[s[left]] -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength