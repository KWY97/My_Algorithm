# 1. itertools 사용하기
# from itertools import permutations
#
# def solution(ability):
#     answer = 0
#     num_students = len(ability)
#     num_sports = len(ability[0])
#
#     students_idx_list = [i for i in range(0, num_students)]
#     candidates = list(permutations(students_idx_list, num_sports))
#
#     for candidate in candidates:
#         score = 0
#         for i in range(num_sports):
#             score += ability[candidate[i]][i]
#         answer = max(answer, score)
#
#     return answer


# 2. 백트래킹 사용하기
def my_dfs(num_check_student, score, ability, check_li):
    global answer
    num_students = len(ability)
    num_sports = len(ability[0])

    if num_check_student == num_sports:
        answer = max(answer, score)
    else:
        for i in range(num_students):
            if check_li[i] == 0:
                check_li[i] = 1
                my_dfs(num_check_student + 1, score + ability[i][num_check_student], ability, check_li)
                check_li[i] = 0


def solution(ability):
    global answer
    num_students = len(ability)
    check_li = [0] * num_students

    my_dfs(0, 0, ability, check_li)
    return answer