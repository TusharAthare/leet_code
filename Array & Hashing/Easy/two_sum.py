from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target -n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
            

if __name__ == "__main__":
    nums = [2,7,11,15,3,12,99,1]
    target_sum = 27
    solution = Solution()
    print(f"{solution.twoSum(nums,target_sum)}")
