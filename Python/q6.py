class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == "" or numRows == 1 or numRows >= len(s):
            return s
        list = ["" for k in range(numRows)]
        zigzagLen = 2 * numRows - 2
        # isdown = 1
        for i in range(len(s)):
            remainder = i % zigzagLen
            if ( remainder < numRows):
                list[remainder]+=s[i]
            else:
                list[2*numRows-2-remainder]+=s[i]

        return ''.join (list)

s = Solution;
print (s.convert( s, "PAYPALISHIRING",3))
