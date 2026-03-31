""" 1. store t frequencies
2. expand right
3. reduce count when char found
4. when count == 0 → window valid
5. shrink from left
6. update minimum length """

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        left = 0
        count = len(t)
        minLen = float('inf')
        start = 0

        for right in range(len(s)):

            if s[right] in countT:
                if countT[s[right]] > 0:
                    count -= 1
                countT[s[right]] -= 1

            while count == 0:

                if right - left + 1 < minLen:
                    minLen = right - left + 1
                    start = left

                if s[left] in countT:
                    countT[s[left]] += 1
                    if countT[s[left]] > 0:
                        count += 1

                left += 1

        if minLen == float('inf'):
            return ""

        return s[start:start+minLen]