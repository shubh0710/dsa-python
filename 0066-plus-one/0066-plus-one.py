class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digit = int("".join(map(lambda x: str(x), digits)))

        plus_one_str_digit = str(str_digit + 1)

        final_digits = list(map(lambda x: int(x), plus_one_str_digit))

        return final_digits