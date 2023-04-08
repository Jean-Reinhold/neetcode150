class Solution:
    """
    O(n) solution
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge case, if anagrams have the same len
        if len(s) != len(t):
            return False
        
        # Go through each letter, one string adds and the
        letter_count = dict()
        for a, b in zip(s, t):
            if a == b:
                continue
            if b not in letter_count:
                letter_count[b] = 0
            if a not in letter_count:
                letter_count[a] = 0
            
            letter_count[a] -= 1
            letter_count[b] += 1
        
        # In the and, the counter should contain only zeros
        return not any(letter_count.values()) 
            
            