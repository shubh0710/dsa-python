class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_of_input = set(nums)

        if len(set_of_input) < len(nums):
            return True
        if len(set_of_input) == len(nums):
            return False