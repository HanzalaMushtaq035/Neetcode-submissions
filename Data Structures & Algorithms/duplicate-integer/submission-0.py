class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            n = nums.count(i)
            if n > 1:
                return True
        return False    