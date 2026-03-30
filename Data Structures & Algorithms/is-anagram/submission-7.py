class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        freqS, freqT = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            freqS[s[i]] += 1
            freqT[t[i]] += 1
        
        return freqS == freqT
