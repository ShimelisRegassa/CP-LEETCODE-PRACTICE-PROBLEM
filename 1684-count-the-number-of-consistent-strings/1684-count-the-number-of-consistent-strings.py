class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        check=set(allowed)
        notallowed=0
        for j in words:
            for i in j:
                if i not in check:
                    notallowed+=1
                    break
        return len(words)-notallowed