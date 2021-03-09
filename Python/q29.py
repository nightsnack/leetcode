MAX_INT = 2**31 - 1
MIN_INT = -2**31

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0

        def duple_divide(dividend, divisor):
            if dividend < divisor:
                return 0
            quotient = 0
            acc = divisor
            while (acc_next := acc+acc) <= dividend:
                acc = acc_next
                quotient+=1
            quotient = 2**quotient + duple_divide(dividend - acc, divisor)
            return quotient

        if dividend>0 and divisor >0 or dividend<0 and divisor<0:
            sign = False
        else:
            sign = True
        quotient = duple_divide(abs(dividend), abs(divisor))
        if sign:
            quotient = -quotient
        if quotient > MAX_INT:
            return MAX_INT

        if quotient < MIN_INT:
            return MIN_INT
        return quotient


dividend = 7
divisor = -3
s = Solution()
print(s.divide(dividend, divisor))
exit(0)

