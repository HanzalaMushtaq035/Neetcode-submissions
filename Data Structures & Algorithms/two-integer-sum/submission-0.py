class Solution(object):
    def twoSum(self, nums, target):
        
        seenMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in seenMap:
                return [seenMap[diff], i]

            seenMap[num] = i

        return []