
A = [2,4,5,7,89,9,2,2,1,2]

def query(A, l, r):
    if l == r:
        return A[l]
    return max(A[l:r + 1])


def logn(A):
    l = 0
    r = len(A) - 1

    # O(logn) * O(1)
    while l < r:
        mid = (l + r)//2

        # O(1) queries
        lq = query(A, l, mid)
        rq = query(A, mid + 1, r)
        # print(lq, rq)
        if lq > rq:
            r = mid
        else:
            l = mid + 1

    if l == 0:
        return query(A, l + 1, len(A) - 1)
    elif l == len(A) - 1:
        return query(A, 0, l - 1)
    
    lmax = query(A, 0, l - 1)
    rmax = query(A, l + 1, len(A) - 1)
    # print(lmax, rmax)
    return max(lmax, rmax)
    

# print(logn(A))
def logn2(A):
    l = 0
    r = len(A) - 1

    twomax = -1000000
    q = query(A, l, r)
    # O(logn) * O(1)
    while l < r:
        mid = (l + r)//2

        # O(1) queries
        lq = query(A, l, mid)
        rq = query(A, mid + 1, r)
        # print(lq, rq)
        if lq == q:
            twomax = max(twomax, rq)
            r = mid
        else:
            twomax = max(twomax, lq)
            l = mid + 1
    return twomax

# print(logn2(A))


def seclar(arr):
    return sorted(arr)[-2]

import random

for i in range(200):
    arr = [_ for _ in range(random.randint(-1,1000))]
    random.shuffle(arr)
    # print(arr, seclar(arr))
    if logn(arr) != seclar(arr):
        print("failed")

