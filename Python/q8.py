class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str=="":
            return 0

        import re
        numstr = re.findall(r"^[+|\-|0-9][0-9]*",str)
        if len(numstr)==0 or numstr[0] in ['+','-']:
            return 0
        else :
            numstr = int (numstr[0])
        # if not gt0:
        #     numstr = -numstr
        if numstr >= 2 ** 31 :
            return 2147483647
        elif numstr <= -2 ** 31 - 1:
            return -2147483648
        else :
            return numstr

s = Solution;
print(s.myAtoi(s,"2147483648"))


