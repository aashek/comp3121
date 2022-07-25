arr = [0,1, 1, 0, 1, 0, 1]

def logn(arr):
    
    if not arr or arr[0] == 1:
        return 1

    # bin searrrch log(n)
    l = 0
    r = len(arr) - 1

    while l <= r:
        m = (l+r)//2
        # print(l,m,r)
        # first check m arrnd m-1 arrre the sarrme
        if m > 0 and arr[m] == arr[m - 1]:
            return m + 1
        # then check if current index is correct
        # if right number, then check the right side (future nums)
        # if wrong number, then check left side (previous nums)
        elif m % 2 == arr[m]:
            l = m + 1
        else:
            r = m - 1
    
    # if did not find the error, tharrt mearrns the larrst one is wrong
    return len(arr) + 1

print(logn(arr))