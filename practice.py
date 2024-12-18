def find_prime_list_under_number(number):
    prime_list = []
    number_list = []

    if M == 1:
        for i in range(2, number + 1):
            number_list.append(i)
    else:
        for i in range(M, number + 1):
            number_list.append(i)

    for num in number_list:
        temp_li = []
        for i in range(2, num + 1):
            if num % i == 0:
                temp_li.append(i)
        if len(temp_li) == 1:
            prime_list.append(num)
    return prime_list

M, N = map(int, input().split())
answer_list = find_prime_list_under_number(N)

for answer in answer_list:
    print(answer)