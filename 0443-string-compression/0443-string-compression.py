class Solution:
    def compress(self, chars: list[str]) -> int:
        left=0
        right=0
        b=len(chars)
        for i in range(1,b+1):
            if(i==b or chars[i]!=chars[left]):
                count=i-left
                chars[right]=chars[left]
                right+=1
                if(count>1):
                    for j in str(count):
                        chars[right]=j
                        right+=1
                left=i
        return right
       