class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        maximum=0
        data={}
        for i in range(len(trips)):
            distance=trips[i][1]
            for j in list(data.keys()):
                if(j <=distance):
                    maximum-=data[j]
                    del data[j]
            maximum+=trips[i][0]
            data[trips[i][2]]=data.get(trips[i][2],0)+trips[i][0]
            if(maximum>capacity):
                return False
        return True

    