class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        c = sorted(c.items(), key=lambda item: item[1])
        return [c[-i][0] for i in range(1, k+1)]