import math
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if s == "" or numRows == 1 or numRows >= len(s):
            return s
        if (numRows == 2):
            b = [s[i] for i in range(len(s)) if i % 2 == 0]
            a = [s[i] for i in range(len(s)) if i % 2 == 1]
            print(''.join(b)+''.join(a))
            return (''.join(b)+''.join(a))
        matrixLen = 2*numRows-2
        znum = math.ceil(len(s)/matrixLen)
        zeronum = matrixLen - len(s)%matrixLen
        s1 = s+'0'*zeronum
        # full = np.zeros((znum,numRows,numRows-1),dtype=object)
        z = [[0]*(numRows-1) for i in range(numRows)]
        full = [z for i in range(znum)]
        for i in range(znum):
            stemp = s1[i*matrixLen:(i+1)*matrixLen]
            # zigzag = np.zeros((numRows, numRows-1), dtype=object)
            zigzag = [[0]*(numRows-1) for i in range(numRows)]
            for t in range(numRows):
                zigzag[t][0] = stemp[t]
            j = numRows
            x = 1

            while j<len(stemp):
                y = numRows - 1 - x
                zigzag[y][x] = stemp[j]
                j+=1
                x+=1
            full[i] = zigzag
        print(full)

        res = ""
        for i in range(numRows):
            for j in range(znum):
                for k in range(numRows-1):
                    if(full[j][i][k]!='0' and full[j][i][k]!=0 ):
                        res += full[j][i][k]
        print(res)
        return res

s = Solution;
s.convert( s, "ABCDE",3)
