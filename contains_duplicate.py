class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appear_count = set()
        for n in nums:
            if n in appear_count:
                return True
            appear_count.add(n)
        return False

    def hashTableContainsDuplicate(self, nums: List[int]) -> bool:
        appear_count = dict()
        for n in nums:
            if n in appear_count:
                return True
            appear_count[n] = 1
        return False
    
    def pythonicContainsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)