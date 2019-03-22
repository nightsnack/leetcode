# Palindrome Number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else :
            s = str(x)
            res = s == s[::-1]


s = Solution;
print(s.isPalindrome(s,100))