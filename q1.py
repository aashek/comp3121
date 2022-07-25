A = [0, 1, 0, 1, 1, 0, 1]


# binary search solution
# log n approach
def solve(A):

    l = 0
    r = len(A) - 1

    while l <= r:
        # find mid
        m = l + (r - l)//2

        # if prev and curr are duplicates
        # return the curr index (1-based)
        if m - 1 >= 0 and A[m] == A[m - 1]:
            return m + 1
        # if the indexed element (0-based)
        # does not equal correct value
        # search left
        elif A[m] == m % 2:
            l = m + 1
        # else search right
        else:
            r = m - 1

    # if l == r
    # return the curr index (1-based)
    return l + 1

import random

assert(solve([0, 1, 0, 1, 1, 0, 1]) == 5)

assert(solve([0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0]) == 10)

assert(solve([0, 0]) == 2)

assert(solve([1, 0, 1, 0]) == 1)

assert(solve([0, 1, 0]) == 4)


n = 100
for i in range(n):
    li = [0, 1] * 50
    ind = random.randint(0,n-1)
    del li[ind]
    assert(solve(li) == ind + 1)


