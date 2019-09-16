class Solution:
    def maxArea(self, height: [int]) -> int:
        i = 0
        j= len(height)-1
        maxa = 0
        while i!=j:
            area = (min(height[i], height[j]) )*(j-i)
            if area > maxa:
                maxa = area
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return maxa

s = Solution;
print(s.maxArea(s,[1,8,6,2,5,4,8,3,7]))