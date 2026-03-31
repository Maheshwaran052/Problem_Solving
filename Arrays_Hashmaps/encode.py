""" Algorithm

Encode

Traverse each string in the list.

Append "length#string" to the result.

Join all encoded strings into one final string.

Example format:

4#neet5#code

Decode

Start from index left = 0.

Move pointer until # to read the length of the string.

Convert that length to integer.

Extract the substring of that length after #.

Add it to result list.

Move left to the start of the next encoded string.

Repeat until the entire string is processed. """

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