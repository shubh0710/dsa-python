class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str_len = len(s)
        result = 0

        for i in range(-1, (-str_len)-1, -1):
            if result == 0 and s[i] == " ":
                continue
            if s[i] != " ":
                result += 1
            if result != 0 and s[i] == " ":
                break

        return result