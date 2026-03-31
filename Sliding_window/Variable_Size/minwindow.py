class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        tMap = {}
        for c in t:
            tMap[c] = tMap.get(c, 0) + 1

        have, need = 0, len(tMap)
        sMap = {}

        res = [-1, -1]
        minLen = float("inf")
        left = 0

        for right in range(len(s)):
            c = s[right]
            sMap[c] = sMap.get(c, 0) + 1

            if c in tMap and sMap[c] == tMap[c]:
                have += 1

            while have == need:
                windowLen = right - left + 1

                if windowLen < minLen:
                    minLen = windowLen   # 🔥 THIS WAS MISSING
                    res = [left, right]

                leftChar = s[left]
                sMap[leftChar] -= 1

                if leftChar in tMap and sMap[leftChar] < tMap[leftChar]:
                    have -= 1

                left += 1

        l, r = res
        return s[l:r+1] if minLen != float("inf") else ""