class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        freq = Counter(planks)
        values = sorted(freq.keys())
        d = len(values)
        pair_width = {}
        for i in range(d):
            vi = values[i]
            fi = freq[vi]
            s = vi + vi
            pair_width[s] = pair_width.get(s, 0) + fi // 2
            for j in range(i + 1, d):
                vj = values[j]
                fj = freq[vj]
                s = vi + vj
                pair_width[s] = pair_width.get(s, 0) + min(fi, fj)
        best = 0
        candidates = set(pair_width.keys()) | set(values)
        for H in candidates:
            total = freq.get(H, 0) + pair_width.get(H, 0)
            best = max(best, total)
        return best