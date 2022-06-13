
def n3(A):
    n = len(A) - 1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if A[i] + A[j] == A[k]:
                    print(A[i], A[j], A[k])
                    return [i+1,j+1,k+1]
    return [-1,-1,-1]


def n2logn(A):
    # merge sort on one element is O(nlogn)
    # extra space O(n)
    B = [(v, i+1) for i,v in enumerate(A)]
    # merge sort on one element is O(nlogn)
    B.sort(key=lambda x:x[0])

    n = len(B) - 1
    for i in range(n):
        for j in range(n):

            target = B[i][0] + B[j][0]
            # binary search O(logn) 
            l = 0
            r = len(B) - 1

            while l < r:
                m = (l + r)//2
                if B[m][0] == target:
                    return [B[i][1], B[j][1], B[m][1]]
                elif B[m][0] < target:
                    l = m + 1
                else:
                    r = m - 1
    return [-1,-1,-1]


def n2(A):
    
    # extra space O(n)
    B = [(v, i+1) for i,v in enumerate(A)]
    # merge sort on one element is O(nlogn)
    B.sort(key=lambda x:x[0])
    # print(B)
    for i in B:
        target = i[0]
        # print(target)
        res = sorted2sum(B, target)
        if res != [-1, -1]:
            res.append(i[1])
            return res
    return [-1,-1,-1]

def sorted2sum(A, target):
    # O(N) runtime
    # O(1) space for constants
    # print(A, target)
    l = 0
    r = len(A) - 1
    while l <= r:
        # print(l, r)
        if A[l][0] + A[r][0] == target:
            return [A[l][1], A[l][1]]
        elif A[l][0] + A[r][0] < target:
            l += 1
        else:
            r -= 1
    
    # if A[l][0] + A[r][0] == target:
            # return [A[l][1], A[l][1]]
    
    return [-1, -1]

A = [2,5,5,1,2,3]
B = [2,5,5,1,2,3]
C = [2,5,5,1,2,3]
print(n2logn(A), n2(B), n3(C)) 


D = [3,3,3,3]
print(n3(D), n2(D)) 