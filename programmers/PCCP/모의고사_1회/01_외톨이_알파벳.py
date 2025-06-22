def solution(input_string):
    count = {}
    answer_list = []

    for idx, char in enumerate(input_string):
        if char not in count:
            count[char] = [idx]
        else:
            count[char].append(idx)

    for key, value in count.items():
        if len(value) >= 2:
            for i in range(len(value) - 1):
                if abs(value[i] - value[i+1]) > 1:
                    answer_list.append(key)
                    break

    if not answer_list:
        answer = 'N'
    else:
        answer = ''.join(sorted(answer_list))

    return answer