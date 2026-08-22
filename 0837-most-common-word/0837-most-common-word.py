class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.strip(".")
        first=paragraph.lower()
        res=[]
        current=[]
        notallowed=set(string.punctuation)|{"\n","\t"," ","\r"}
        for i in first:
            if i in notallowed:
                if(current):
                    res.append("".join(current))
                    current=[]
            else:
                current.append(i)
        if(current):
            res.append("".join(current))
        for i in banned:
            i=i.lower()
        ob=Counter(res)
        fre=dict(sorted(ob.items(),key=lambda x:-x[1]))
        for i in fre:
            if i not in banned:
                return i

        