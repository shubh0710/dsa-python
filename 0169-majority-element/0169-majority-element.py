class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        nums_dict = Counter(nums)
        helper = 0
        output = 0

        for i in nums_dict:
            if nums_dict[i] > helper:
                helper = nums_dict[i]
                output = i

        return output