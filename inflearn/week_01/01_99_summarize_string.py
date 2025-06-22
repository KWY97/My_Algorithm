# Q.
# 1. 입력으로 소문자의 알파벳이 입력됩니다.
# 2. 각 알파벳은 중복이 가능합니다.
# 3. 중간에 없는 알파벳이 있을 수도 있습니다.
# 입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.

# 문제의 번호별 조건에 대한 입력 예시와 출력
# Ex 1)
# abc
# a1/b1/c1

# Ex 2-1)
# aaabbbc
# a3/b3/c1

# Ex 2-2)
# abbbc
# a1/b3/c1

# Ex 3-1)
# ahhhhz
# a1/h4/z1

# Ex 3-2)
# acccdeee
# a1/c3/d1/e3


# 내 풀이
def summarize_string(input_str):
    for char in input_str:
        for i in range(len(alphabet_list)):
            if char == alphabet_list[i]:
                count_list[i] += 1

    for j in range(len(count_list)):
        if count_list[j] != 0:
            answer_list.append(chr(j + 97) + str(count_list[j]))

    return ('/'.join(answer_list))

count_list = [0] * 26
input_str = "accdzsdascdeee"
alphabet_list = []
answer_list = []

for i in range(97, 123):
    alphabet_list.append(chr(i))

print(summarize_string(input_str))