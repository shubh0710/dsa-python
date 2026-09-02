class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_list_s = sorted(s)
        sorted_list_t = sorted(t)

        if sorted_list_s == sorted_list_t:
            return True
        else:
            return False