class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1

        for i in range(len(nums)):
            if nums[i] == nums[-1]:
                break
            elif i + 1 <= len(nums) - 1 and not nums[i + 1] > nums[i]:

                target_index = None

                for j in range(i, len(nums)):
                    if nums[j] > nums[i]:
                        target_index = j
                        break

                if target_index != None:
                    nums[i + 1] = nums[target_index]
                    k += 1

            elif i + 1 <= len(nums) - 1 and nums[i + 1] > nums[i]:
                k += 1

        return k