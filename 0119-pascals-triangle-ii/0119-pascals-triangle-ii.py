class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [1]
        for i in range(rowIndex):
            res.append(1)
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j - 1]
        return res