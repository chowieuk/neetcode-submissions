# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, L: List[Pair], R: List[Pair]) -> List[Pair]:

        result = []
        i, j = 0, 0

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        
        if i == len(L):
            result.extend(R[j:])
        else:
            result.extend(L[i:])

        return result

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2

        L = self.mergeSort(pairs[:m])
        R = self.mergeSort(pairs[m:])

        return self.merge(L,R)