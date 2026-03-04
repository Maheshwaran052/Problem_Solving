# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         hashMap1 = {}
#         hashMap2 = {}
#         if len(s) != len(t) :
#             return False
#         for char in s:
#             if char in hashMap1:
#                 hashMap1[char] += 1
#             else:
#                 hashMap1[char] = 1
        
#         for char in t:
#             if char in hashMap2:
#                 hashMap2[char] += 1
#             else:
#                 hashMap2[char] = 1
#         return hashMap1 == hashMap2

# Algorithm
""" 1. First we add count of all characters in first Str to hashmap
2. Next we try removing all characters in second str from hashmap
3. if extra character is there or the hashmap is not empty then its not anagram
4. if hashmap gets empty then anagram
 """
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        if len(s) != len(t) :
            return False
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        
        #decrement all. if hashmap becomes empty anagram
        for char in t:
            if(char not in hashMap):
                return False
            hashMap[char] = hashMap.get(char,0) - 1
            if(hashMap[char]==0):
                del hashMap[char]
        return len(hashMap) == 0
        
        