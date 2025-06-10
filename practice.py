def get_lines(n, w):
    lines = -(-n // w)
    return lines

def solution(n, w, num):
    lines = get_lines(n, w)
    answer = 1
    boxes = []
    cur = 1

    for i in range(lines):
        if i % 2 == 0:
            # 정순으로
            for j in range(cur, cur + w):
                boxes.append(j)
            cur += w
        else:
            # 역순으로
            for j in range(cur + w -1, cur - 1, -1):
                boxes.append(j)
            cur += w

    for temp_num in range(cur-1, n, -1):
        boxes[boxes.index(temp_num)] = 0

    num_index = boxes.index(num)
    next_index = num_index + w

    while next_index < cur-1:
        if boxes[next_index] == 0:
            break

        answer += 1
        next_index += w

    return answer

print(solution(6, 5, 4))