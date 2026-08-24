class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff=[0]*(n+1)
        for x,y,z in bookings:
            diff[x-1]+=z
            diff[y]-=z
        res=[0]*n
        total=0
        for i in range(n):
            total+=diff[i]
            res[i]=total
        return res

