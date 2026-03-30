class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we can use the sorted str as a key in a map of str to List[str]
        # then return the list of the map
        # note that sorted(str) is a list, which cannot be a key (as it's mutable)

        hm = defaultdict(list)

        for s in strs:
            hm[tuple(sorted(s))].append(s)
        
        return(list(hm.values()))