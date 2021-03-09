class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        """

        iterate the num1 and num2:

            convert both nums to in by ord

        curr1 curr2 = 0
        current = current * 10 + ord(num) - ord("0")

        return str(curr1 * curr2)

        """

        int1, int2 = 0, 0

        for i in range(len(num1)-1, -1, -1):
            int1 += (ord(num1[len(num1)-1-i])-ord('0'))*(10**i)

        for i in range(len(num2) - 1, -1, -1):
            int2 += (ord(num2[len(num2) - 1 - i]) - ord('0')) * (10 ** i)

        product = int1 * int2

        return str(product)

s = Solution()
num1 = "123"
num2 = "456"
print(s.multiply(num1, num2))