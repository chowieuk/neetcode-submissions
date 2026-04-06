# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, left: List[Pair], right: List[Pair]) -> List[Pair]:
        result = []
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        if i == len(left):
            result.extend(right[j:])
        else:
            result.extend(left[i:])

        return result



    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:

        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2

        L = self.mergeSort(pairs[:m])
        R = self.mergeSort(pairs[m:])

        return self.merge(L,R)
