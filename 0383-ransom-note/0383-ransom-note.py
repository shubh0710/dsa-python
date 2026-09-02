class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter

        magazine_dict = Counter(magazine)
        ransomNote_dict = Counter(ransomNote)
        helper = 0

        for ch in ransomNote:
            if ch in magazine and ransomNote_dict[ch] <= magazine_dict[ch]:
                helper += 1

        if helper == len(ransomNote):
            return True
        elif helper < len(ransomNote):
            return False