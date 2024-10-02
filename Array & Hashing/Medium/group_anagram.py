from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sol = defaultdict(list)

        for word in strs:
            sorted_word = sorted(word)
            sol[''.join(sorted_word)].append(word)
        return sol.values()