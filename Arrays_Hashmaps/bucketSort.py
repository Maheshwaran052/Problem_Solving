#1. Bucket sort for top k freuqnet elements
""" Algorithm
1. First take a hashmap store all the numbers with their count
2. create n+1 buckets and store in a list
3. append the hashmap key(number),value(frequency) into buckets[freq].append(num)
4. Then traverse the buckets list from n+1 until top k elements are fetched. """

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        # count frequency
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        # fill buckets
        for num, freq in hashMap.items():
            buckets[freq].append(num)

        result = []

        # traverse from high freq to low
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num) #if num = [] it will automatically skip so no worries
                if len(result) == k:
                    return result