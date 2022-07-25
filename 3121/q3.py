# 3.1 = 14

# 3.2

# cannot use j 
# there msut be at least one value after jth element that is less than possible i values

# max(i..j+1)

arr = [1,10,9,5,7,3,8,2,6,4]

# 3 arrays

def solution(arr):

    # stairs = []
    # stair = []
    # for i in range(1, len(arr) - 1):
    #     if arr[i] > arr[i-1] and up:
    #         up = False
    #         stairs.append(stair)
    #         stair = []
    #     stair.append(arr[i])

    stairs = [[1,10], [10,9,5], [5,7], [7,3], [3,8], [8,2], [2,6], [6,4]]


    sum_arr = []
    for j in stairs:
        # if descending
        print(j)
        t = []
        if j[0] > j[1]:
            ma = len(j) - 1
            for x in j:
                x *= ma
                ma -= 1
                t.append(x)
        else:
            ma = 0
            for x in j:
                print(ma)
                x *= ma
                print(x)
                ma += 1
                t.append(x)
        sum_arr.append(sum(t))
    print(stairs)
    print(sum_arr)

    


solution(arr)