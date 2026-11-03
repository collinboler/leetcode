class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        # (LeetDuck) Which values of i does this loop include?
        # (LeetDuck) n is an int; len(n) will fail.
        for i in range(1, n + 1):
            if i % 15 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer
