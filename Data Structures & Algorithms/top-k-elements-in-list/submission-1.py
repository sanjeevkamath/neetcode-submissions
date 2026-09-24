class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        new_count = sorted(count.keys(), key=lambda num: count[num], reverse = True)
        
        return new_count[:k]