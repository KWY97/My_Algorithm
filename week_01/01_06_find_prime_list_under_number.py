# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다. (1은 소수가 아니다.)

input = 20

# # 1차 풀이
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for n in range(2, number + 1):
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#     return prime_list


# # 2차 풀이 (1차 풀이 개선 ver)
# def find_prime_list_under_number(number):
#     prime_list = []
#
#     for n in range(2, number + 1):
#         for i in prime_list:
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)
#     return prime_list


# 3차 풀이 (2차 풀이 개선 ver)
def find_prime_list_under_number(number):
    prime_list = []

    for n in range(2, number + 1):
        for i in prime_list:
            if i * i <= n and n % i == 0:
                break
        else:
            prime_list.append(n)
    return prime_list


result = find_prime_list_under_number(input)
print(result)