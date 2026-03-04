""" Algorithm
1. to group the anagrams first we need to traverse each word in list of strings
2. Then we need a hashmap to store these anagrams in key,value pair
3. Key: for example we have "eat" and "ate", the key is sorted to "aet".
4. then we append the word to this key thus getting grouped anagrams """

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for word in strs:
            #sort the letters to compare for anagrams
            key = "".join(sorted(word))
            hashMap.setdefault(key,[]).append(word)
        return list(hashMap.values())