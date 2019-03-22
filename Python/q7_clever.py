class Solution:
    def reverse(self, x: int) -> int:
        gt0 = 1
        if (x<0):
            x = -x
            gt0 = 0
        x = str(x)
        x = int(x[::-1])
        if (gt0 ==0):
            x = -x
        if x > 2 ** 31 or x < -2 ** 31 - 1:
            return 0
        return x

solution = Solution;
print(solution.reverse(solution,-12300))