# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.

input = 2

def find_prime_list_under_number(number):
    prime_list = []
    number_list = []

    for i in range(2, number + 1):
        number_list.append(i)

    if number == 1:
        return '입력은 1보다 커야합니다.'
    else:
        for num in number_list:
            temp_li = []
            for i in range(2, num + 1):
                if num % i == 0:
                    temp_li.append(i)
            if len(temp_li) == 1:
                prime_list.append(num)
    return prime_list

result = find_prime_list_under_number(input)
print(result)