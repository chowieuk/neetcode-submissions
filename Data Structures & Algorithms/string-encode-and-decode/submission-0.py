from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        k = 0
        while i < len(s):
            # we are looking for, but haven't found the delimiter
            if not s[i] == "#":
                 i += 1
                 k += 1
                 continue
            # we have found an instance of the delimiter
            else:
                strLen = int(s[i - k: i])
                i = i + 1
                res.append(s[i :i + strLen])
                k = 0
                i = i + strLen
        return res