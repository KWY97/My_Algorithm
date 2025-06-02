T = int(input())

for tc in range(1, T+1):
    n = int(input())
    product_list = list(map(int, input().split()))

    sum_cost = 0
    max_val = 0

    for i in range(n-1, -1, -1):
        if product_list[i] > max_val:
            max_val = product_list[i]
        else:
            sum_cost += max_val - product_list[i]

    print(f'#{tc} {sum_cost}')