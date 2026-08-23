class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ob=defaultdict(list)
        for i in strs:
            val=[0]*26
            for j in i:
                val[ord(j)-ord("a")]+=1
            ob[tuple(val)].append(i)
        return list(ob.values())

    

    
       

        

       

