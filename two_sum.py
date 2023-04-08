class Solution:
    """
    Given that target = a + b

    Lets store a = target - b so if you find 
    the complementary, the problem is solved.

    This guarantees a O(n) if your hashmap is well
    implemented

    Edge cases are:
        empty list: covered by for
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffHolder = dict()
        
        for i, b in enumerate(nums):
            a = target - b
            # Means we found the complementary
            if a in diffHolder:
                return [diffHolder[a], i]
            diffHolder[b] = i
        
        return []