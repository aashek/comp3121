import random

arr = [_ for _ in range(1, 19)]
random.shuffle(arr)

print(arr)


def solution(arr, x):
    # nlogn
    B = sorted(arr)
    for val in B:
        l = 0
        r = len(B) - 1
        target = x - val
        while l <= r:
            m = (l + r) // 2
            if target == B[m]:
                return True 
            elif B[m] < target:
                l = m + 1
            else:
                r = m - 1
    return False

def sol(arr, x):
    seen = {}
    for i in arr:
        target = x - i
        if target in seen:
            return [i, seen[target]]
        seen[target] = i
    print(seen)
    return False




print(solution(arr, 35))
print(sol(arr, 35))