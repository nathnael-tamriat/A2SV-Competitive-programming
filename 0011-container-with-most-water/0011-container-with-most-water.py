class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0, len(height) - 1
        area = 0
        while i < j:
            min_h = min(height[i],height[j])
            area = max(area,(j-i )* min_h)
            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return area