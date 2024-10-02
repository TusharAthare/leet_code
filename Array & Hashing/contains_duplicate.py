from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            s.add(i)
        return False
    
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)