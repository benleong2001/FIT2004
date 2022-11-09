from itertools import count
from math import inf

#%% Coin Change Problem
def coin_chg_prob(N: int, coins: list[int]) -> list[int]:
    count_arr = [inf] * (N + 1)
    count_arr[0] = 0
    for num in range(1, N + 1):
        for coin in coins:
            total = num - coin
            if total >= 0 and (new_count := count_arr[total] + 1) < count_arr[num]:
                count_arr[num] = new_count

    return count_arr

x = coin_chg_prob(12, [1, 5, 6, 9])
print(x)

#%% Knapsack (Unbounded)
def knapsack_unbnd(cap: int, items: list[(int, int)]):
    pass