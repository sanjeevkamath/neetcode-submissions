class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Check if value is within row
        # Check within row if value is present
        bot = 0
        top = len(matrix) - 1

        width = len(matrix[0]) - 1

        while bot <= top:
            mid = (top + bot) // 2

            if matrix[mid][0] <= target and matrix[mid][width] >= target:
                # Check subarray
                l = 0
                r = width
                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] > target:
                        r = m - 1
                    elif matrix[mid][m] < target:
                        l = m + 1
                return False
                                   
            elif matrix[mid][0] > target:
                top = mid - 1
            elif matrix[mid][width] < target:
                bot = mid + 1
        return False
                
            