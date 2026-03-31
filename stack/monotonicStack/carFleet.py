from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleet = 0
        #combine position and speed pairs into single list
        cars = list(zip(position, speed))

        #sort in descending order using position (x[0])
        cars.sort(key = lambda x:x[0],reverse=True) 

        for pos,s in cars:
            current_time = (target - pos)/s

            if not stack or current_time > stack[-1]:
                stack.append(current_time)
        return len(stack)

