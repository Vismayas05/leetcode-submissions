class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     for i in range(len(nums)):
        for j in range(i+1,ken(nums)):
            if nums[1] == nums[j]:
                return True