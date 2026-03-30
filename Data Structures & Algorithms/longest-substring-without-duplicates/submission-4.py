class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not len(s): return 0
        l, r = 0, 1
        maxSub = 1
        seen = set(s[l])
        while r < len(s):
            if not s[r] in seen:
                seen.add(s[r])
                maxSub = max(maxSub, len(seen))
                r += 1
            elif s[r] == s[l]:
                seen.remove(s[l])
                l += 1
            else:
                l = r
                r += 1
                seen = set(s[l])
        return maxSub