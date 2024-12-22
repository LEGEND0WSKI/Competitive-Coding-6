# // Time Complexity :O(nlogk) binary search +  find kth smallest in all columns
# // Space Complexity :O(1) no extra space
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Left to right + bottom up scan logic


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        def lessThanK(matrix, target):          # find the total count of elements under the give count in the matrix
            n = len(matrix[0])
            cnt = 0
            i = n-1
            j = 0

            while (i >= 0 and j < n):           # bottom left to top right scan
                if matrix[i][j] > target:
                    i-=1
                else:
                    cnt = cnt + i + 1
                    j+=1
            return cnt
        
        # binary search on matrixx
        low = matrix[0][0]
        high = matrix[-1][-1]
        count = 0
        while low < high:
            mid = low + (high-low)//2  
            count = lessThanK(matrix, mid)      
            if count < k:
                low = mid + 1
            else:
                high = mid
        return low
