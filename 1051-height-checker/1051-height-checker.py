class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        num=sorted(heights)
        counter=0
        for i in range(len(heights)):
            if(num[i]!=heights[i]):
                counter+=1
        return counter
        