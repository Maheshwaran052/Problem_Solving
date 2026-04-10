from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        low,high = 0,len(matrix[0])-1
        #find which row the target exists

        for row in range(m):
            if(matrix[row][0]<= target < matrix[row][len(matrix[row]) - 1]):
                #Perform binary search here
                while low <= high:
                    mid = (low + high)//2

                    if(matrix[row][mid] == target):
                        return True
                    elif(matrix[row][mid] < target):
                        low = mid + 1
                    else:
                        high = mid - 1
                return False
            else:
                continue
        return False
            

