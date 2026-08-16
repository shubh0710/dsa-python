class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        helper_arr = [0,0]
        x = len(s)

        if x > 1:
            if x % 2 != 0:
                y = -1
                for i in range((x-1)//2):
                    helper_arr[0] = s[i]
                    helper_arr[1] = s[y]
                    s[i] = helper_arr[1]
                    s[y] = helper_arr[0]
                    y -= 1

            if x % 2 == 0:
                y = -1
                for i in range(x//2):
                    helper_arr[0] = s[i]
                    helper_arr[1] = s[y]
                    s[i] = helper_arr[1]
                    s[y] = helper_arr[0]
                    y -= 1