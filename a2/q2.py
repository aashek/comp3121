
prices = [9,7,8,6,5,6,9,9,9,4,3,2]

print('\n'.join([f"It costs {prices[i]} to purchase a ration at Town {i+1}" for i in range(len(prices))]))

cost   = 0
lowest = 10000

# print(prices)
for i,v in enumerate(prices):
    print()
    print(f'Current Town is {i+1} and lowest price seen is {lowest}')
    print(f'Visiting Town {i+1}, and checking price')
    print(f'Price is {v}')
    print()
    if v < lowest:
        lowest = v
        print(f'swapped to Town {i+1}')

    cost += lowest
    print(f'Current cost to Town {i+2} is {cost}')


print(f"Minimum cost from Town 1 to Town {len(prices) + 1} is {cost}")
    