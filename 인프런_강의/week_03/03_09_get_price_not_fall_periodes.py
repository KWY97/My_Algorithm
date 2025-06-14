prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    n = len(prices)
    result = [0] * n

    for i in range(n-1):
        price_not_fall_period = 0
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                price_not_fall_period += 1
            else:
                price_not_fall_period += 1
                break

        result[i] = price_not_fall_period

    return result


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))