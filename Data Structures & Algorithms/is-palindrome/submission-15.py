import math


class Solution:
    def isPalindrome(self, s: str) -> bool:

        stripped = re.sub(r'[^a-zA-Z0-9]', '', s)
        print(stripped)
        start = 0
        end = len(stripped) - 1
        middle = math.floor(len(stripped) / 2)

        while start < middle:
            if stripped[start].casefold() != stripped[end].casefold():
                print(start,end,stripped[start].casefold(),stripped[end].casefold())
                return False
            start += 1
            end -= 1
        return True
