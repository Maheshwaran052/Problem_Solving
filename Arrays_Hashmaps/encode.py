from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s)) + '#' + s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        result = []
        left = 0
        
        while left < len(s):
            right = left
            
            # move until '#'
            while s[right] != '#':
                right += 1
            
            length = int(s[left:right])
            right += 1
            
            word = s[right:right+length]
            result.append(word)
            
            left = right + length
        
        return result