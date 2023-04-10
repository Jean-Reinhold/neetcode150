class Solution:
    """
    The hack here is the signature of a family of anagrams. 

    Each signature is a vector of the count of letters from a-z

    use the inner for loop to calculate the signature, then update it
    in a hash table
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return ans.values()

            