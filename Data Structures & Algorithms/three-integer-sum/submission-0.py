class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        matches = []
        sorted_nums = sorted(nums)

        for i in range(0,len(sorted_nums)-1):
            # Skip duplicate starting numbers
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            diff = 0 - sorted_nums[i]
            j = i + 1
            k = len(sorted_nums) - 1
            while j < k:
                if sorted_nums[j] + sorted_nums[k] == diff:
                    matches.append([sorted_nums[i],sorted_nums[j],sorted_nums[k]])
                    j += 1
                    k -= 1
                    # Skip duplicate inner numbers
                    while j < k and sorted_nums[j] == sorted_nums[j - 1]:
                        j += 1
                elif sorted_nums[j] + sorted_nums[k] > diff:
                    k -= 1
                else:
                    j += 1
        
        return matches


