# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.

# 방법 1
# 하나의 원소를 다른 원소들과 비교해서 최대값인지 분석하는 방법
# 각 숫자마다 모든 다른 숫자와 비교해서 최대값인지 확인
# 만약 다른 모든 값보다 크다면 반복문을 중단
# 하지만 2중 for문을 돌아야 하므로 방법 2가 더 적절한 방법임 !
def find_max_num(array):
    for num in array:
        is_max_num = True
        for compare_num in array:
            if num < compare_num:
                is_max_num = False
        if is_max_num:
            return num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))


# 방법 2
# 하나의 변수를 잡아서 그 변수와 비교하며 가장 큰 수를 찾는 방법
# 배열 내에서 가장 큰 수를 찾아야 합니다.
# 그러면, 가장 큰 수를 저장할 변수를 만들고, 배열을 돌아가면서 그 변수와 비교
# 만약 값이 더 크다면, 그 변수에 대입
def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    return max_num

print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))