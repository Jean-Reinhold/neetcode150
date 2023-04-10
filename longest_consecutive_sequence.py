class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # convert it for in operation O(1)
        
        longest = 0
        for n in nums:
            # Look for a sequence of at least len = 2
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest