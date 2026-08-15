class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)

        k = m

        for i in range(m, len(nums1)):
            if nums1[i] != 0:
                nums1[k] = nums1[i]
                k += 1

        if n > 0:
            x = 0

            while x > -n:
                nums1.pop()
                x -= 1

        nums1.sort()
