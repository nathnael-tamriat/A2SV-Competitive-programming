class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        #using binary search
        
        left = 0
        right = int(c ** 0.5)
        while left <= right:
            if left**2 + right**2 == c:
                return True
            elif left ** 2 + right ** 2 < c:
                left +=1
            else:
                right -= 1

        return False
