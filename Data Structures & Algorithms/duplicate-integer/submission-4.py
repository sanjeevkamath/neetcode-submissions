class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing = {}

        for num in nums:
            if num in existing:
                return True
            existing[num] = 1
        return False