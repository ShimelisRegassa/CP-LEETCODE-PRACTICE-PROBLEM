class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        m=0
        n=len(people)-1
        num=0
        while(m<=n):
            if(people[m]+people[n] <=limit):
                m+=1
                n-=1
                num+=1
            else:
                n-=1
                num+=1
        return num


        