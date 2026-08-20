class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        num1=set()
        win=[]
        win1=[]
        result=[]
        loser_count={}
        for x,y in matches:
            num1.add(x)
            loser_count[y]=loser_count.get(y,0)+1
        for x in num1:
            if x not in loser_count.keys():
                win.append(x)
        for x,y in loser_count.items():
            if(y==1):
                win1.append(x)          
        win.sort()
        win1.sort()
        result.insert (0,win)
        result.insert(1,win1)
        return result
        