class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #sorting using bubble sort
        for i in range(0,len(names)-1):
            for j in range(0,len(names)-i-1):
                if heights[j] < heights[j+1]:
                    names[j],names[j+1] = names[j+1],names[j]
                    heights[j],heights[j+1] = heights[j+1], heights[j]
        return names