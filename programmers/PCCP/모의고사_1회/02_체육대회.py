from itertools import permutations

def solution(ability):
    answer = 0
    num_students = len(ability)
    num_sports = len(ability[0])

    students_idx_list = [i for i in range(0, num_students)]
    candidates = list(permutations(students_idx_list, num_sports))

    for candidate in candidates:
        score = 0
        for i in range(num_sports):
            score += ability[candidate[i]][i]
        answer = max(answer, score)

    return answer