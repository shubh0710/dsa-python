class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1_len, word2_len = len(word1), len(word2)
        bigger_word = max(word1_len, word2_len)

        for i in range(bigger_word):
            if word1_len > word2_len:
                result += word1[i]
                if (i+1) > word2_len:
                    continue
                result += word2[i]
                continue

            if word2_len > word1_len:
                if (i+1) > word1_len:
                    result += word2[i]
                if (i+1) <= word1_len:
                    result += word1[i]
                    result += word2[i]
                    continue

            if word1_len == word2_len:
                result += word1[i]
                result += word2[i]

        return result