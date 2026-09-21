class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Maintain, current max product, current min product
        prevMax = 1
        prevMin = 1
        maxNum = float("-inf")

        for num in nums:
            currentMin = min(num, num * prevMin, num * prevMax)
            currentMax = max(num, num*prevMin, num * prevMax)

            if maxNum < currentMax:
                maxNum = currentMax
            
            prevMax = currentMax
            prevMin = currentMin
        return maxNum


            

