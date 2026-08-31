class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        input_list_set = set(nums)
        element_list_dict = {v: i for i, v in enumerate(nums)}
        output = []

        for i in range(len(nums)):
            if (target - nums[i]) in input_list_set and i != element_list_dict[(target - nums[i])]:
                output.append(i)
                output.append(element_list_dict[(target - nums[i])])
                break

        return output