class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}

        for i in range(len(nums)):
            numB = target - nums[i]
            if numB not in numHash:
                numHash[nums[i]] = i
            else:
                return [numHash[numB], i]