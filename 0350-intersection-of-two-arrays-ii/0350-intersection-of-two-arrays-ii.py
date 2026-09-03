class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        nums1_dict = Counter(nums1)
        nums2_dict = Counter(nums2)
        output = []
        helper = 0
        prev = None

        for i in sorted(nums1):
            if i != prev:
                helper = 0
                prev = i
            if i in nums2 and helper < min(nums1_dict[i], nums2_dict[i]):
                output.append(i)
                helper += 1

        return output