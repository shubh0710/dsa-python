class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        dict = Counter(s)

        for i in range(len(s)):
            if s[i] in dict and dict[s[i]] == 1:
                return i

        return -1