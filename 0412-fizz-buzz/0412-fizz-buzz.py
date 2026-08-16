class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [0] * n

        for i in range(n):
            if (i+1) >= 3 and (i+1) % 3 == 0 and (i+1) % 5 != 0:
                result[i] = "Fizz"

            if (i+1) >= 5 and (i+1) % 5 == 0 and (i+1) % 3 != 0:
                result[i] = "Buzz"

            if (i+1) >= 15 and (i+1) % 5 == 0 and (i+1) % 3 == 0:
                result[i] = "FizzBuzz"

            if (i+1) % 5 != 0 and (i+1) % 3 != 0 :
                result[i] = str(i+1)
  
        return result