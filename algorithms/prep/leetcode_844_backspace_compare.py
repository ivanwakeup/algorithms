'''
solve with pointers and constant space:

approach:
why can't we start at the beginning? there wouldn't be a good way to compare if things are equal
without the extra space this way.

start from the right end
if chars, compare them. keep track of backspaces
if we have any backspaces when we hit a char, we need to skip the next char
'''


class Solution:
    def backspaceCompare(self, s1, s2):
        if not s1 or not s2:
            return not s1 and not s2

        i = len(s1) - 1
        j = len(s2) - 1
        b1 = 0
        b2 = 0
        while i >= 0 and j >= 0:
            while i > 0:
                if s1[i] == "#":
                    i -= 1
                    b1 += 1
                elif s1[i] != "#" and b1:
                    i-=1
                else:
                    break
            while s2[j] == "#":
                j -= 1
                b2 += 1
            # now account for backspaces
            while b1:
                i-=1
                b1-=1
                if i>=0 and s1[i] == "#":
                    b1+=1
                    i-=1
            while b2:
                j-=1
                b2-=1
                if j >=0 and s2[j] == "#":
                    b2+=1
                    j-=1
            if i < 0 or j < 0:
                return i < 0 and j < 0
            if i >= 0 and j >= 0 and s1[i] != s2[j]:
                return False
            i -= 1
            j -= 1

        b1 = 0
        b2 = 0
        while i >= 0 and s1[i] == "#":
            b1 += 1
            i -= 1
        i -= b1
        while j >= 0 and s2[j] == "#":
            b2 += 1
            j -= 1
        j -= b2

        return i < 0 and j < 0


sol = Solution()

sol.backspaceCompare("bxj##tw", "bxj###tw")

"bxj##tw"
"bxj###tw"