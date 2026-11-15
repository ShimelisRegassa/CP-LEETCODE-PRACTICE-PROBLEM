class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        counter=0
        last=0
        for x,y in meetings:
            if(x>last+1):
                counter+=(x-last-1)
            last=max(last,y)
        if(days>last):
            counter+=days-last
        return counter

      
