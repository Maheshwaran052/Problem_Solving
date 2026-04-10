from collections import defaultdict
from typing import List

class TimeMap:

    def __init__(self):
        self.store = defaultdict(List)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))
        # {key1 :[(1,"a"),(2,"b"),(3,"c")],key2:[(1,"a"),(2,"b"),(3,"c")]}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
    
        arr = self.store[key]
        left, right = 0, len(arr) - 1
        res = ""   # store best possible answer

        while left <= right:
            mid = (left + right) // 2
            ts, val = arr[mid]

            if ts == timestamp:
                return val
        
            if ts < timestamp:
                res = val          # ✅ possible answer
                left = mid + 1     # go right (maybe better)
            else:
                right = mid - 1    # go left
    
        return res



        
