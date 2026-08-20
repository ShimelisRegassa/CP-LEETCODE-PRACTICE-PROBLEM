class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lost={}
        winner={}
        for j in range(len(matches)):
            lost[matches[j][1]]=lost.get(matches[j][1],0)+1
            winner[matches[j][0]]=winner.get(matches[j][0],0)+1
        lst1=[]
        lst2=[]

        for j  in winner:
            if j not in lost:
                lst1.append(j)
            elif j in lost and lost[j]==1:
                lst2.append(j)
            else:
                continue
        for j in lost:
            if( j not in winner and lost[j]==1):
                lst2.append(j)

        return sorted(lst1),sorted(lst2)
            

