class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ref = {}
        for counter, num in enumerate(nums):
           if target - num in ref:
              return (ref[target - num], counter)
           ref[num] = counter