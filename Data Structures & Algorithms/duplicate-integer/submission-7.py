class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      for i in range(nums):
        for j in range(i+1,(nums)):
            if nums(i)==nums(j):
                return true
      return false
      