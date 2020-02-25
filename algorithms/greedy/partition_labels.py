from typing import List
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        idxs = {}
        for i, char in enumerate(S):
            idxs[char] = i

        hi = idxs[S[0]]
        result = []
        prefix_sum = 0
        for lo in range(len(S)):
            if lo == hi:
                result.append(lo + 1 - prefix_sum)
                prefix_sum = prefix_sum + result[-1]
            elif idxs[S[lo]] > hi:
                hi = idxs[S[lo]]

        return result

sol = Solution()
sol.partitionLabels("ababcbacadefegdehijhklij")