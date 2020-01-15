'''
".L." -> "LL."

".RLLLLR" -> ".RLLLLR"

"RLRLRL" -> "RLRLRL"


we can use a sliding window approach i think

"....R" => "....R"
"....LR" => "LLLLLR"


we increase our window size from the left, until we find either:
    L => all dominos from the lo pointer to the current L become L
    R => we reset our lo pointer to


our sliding window has a few cases:
    1. we make a window of some blanks followed by L -> everything becomes L
    2. we make a window of some blanks followed by R -> nothing happens and we reset LO to where R is
    3. we make a window of L + some blanks + R -> nothing changes, we resert LO to where R is
    4. we make a window or R + some blanks + L -> we update what is in between bringing the pointers closer together


refine it:
 if we first encounter R, just reset LO to where R is
 if we first encounter L, move LO forward while updating everything to L
 also keep CUR which keeps track of what element the beginning of our window is. we use this to determine the behavior when we encounter another
 L or R.


pseudo:
init LO, HI
while HI < len(dominoes):
    if hi is not R or L move it forward
    else:
        maybeFill()?
        reset LO = HI
    hi += 1

maybeFill:
    if HI == L:
        fill
    else:
        reset LO

two different fill cases:
LO == R, in which case we fill by trading off filling from hi and low
LO == . or L -> just L fill from the bottom


'''



def pushDominoes(dominoes):
    lo, hi = 0, 0
    d = list(dominoes)
    chk = {"L", "R"}
    while hi < len(d):
        # window needs to be filled or we might have a postfix like "R....", so fill it
        if d[hi] in chk or hi == len(d) - 1:
            do_fill(lo, hi, d)
            lo = hi
        hi += 1

    return "".join(d)

def do_fill(lo, hi, d):
    if d[hi] == "L":
        if d[lo] == "R":
            # window is Rs from the left and Ls from the right
            while lo < hi:
                d[lo] = "R"
                d[hi] = "L"
                lo += 1
                hi -= 1
        else:
            # window is completely L
            while lo <= hi:
                d[lo] = "L"
                lo += 1
    elif d[lo] == "R":
        # window is completely R
        while lo <= hi:
            d[lo] = "R"
            lo += 1

assert(pushDominoes("R...L") == "RR.LL")