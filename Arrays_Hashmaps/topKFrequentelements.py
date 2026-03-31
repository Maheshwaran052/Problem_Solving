""" Algorithm

Create a hashmap to count the frequency of each number in the array.

Create a bucket list where index represents the frequency.

Traverse the hashmap and place each number in the bucket corresponding to its frequency.

Traverse the bucket list from highest frequency to lowest.

Collect numbers into the result list until k elements are obtained.

Return the result. """

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
                result.append(num)
                if len(result) == k:
                    return result