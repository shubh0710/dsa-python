class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        k = 0
        result = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                k += 1
            if nums[i] == 0 or i == len(nums) - 1:
                if k > result:
                    result = k
                k = 0

        return result