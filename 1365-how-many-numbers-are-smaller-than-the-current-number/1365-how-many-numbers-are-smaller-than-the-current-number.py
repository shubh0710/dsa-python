class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []

        for i in nums:
            k = 0
            for j in nums:
                if i > j:
                    k += 1
            result.append(k)

        return result