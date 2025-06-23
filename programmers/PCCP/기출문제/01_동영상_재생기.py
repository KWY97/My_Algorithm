def change_to_second(time):
    second = 0
    second = int(time[0:2]) * 60 + int(time[3:5])
    return second

def solution(video_len, pos, op_start, op_end, commands):
    answer = ''

    video_len_second = change_to_second(video_len)
    pos_second = change_to_second(pos)
    op_start_second = change_to_second(op_start)
    op_end_second = change_to_second(op_end)

    if op_start_second <= pos_second <= op_end_second:
        pos_second = op_end_second

    for command in commands:
        if command == 'prev':
            if pos_second < 10:
                pos_second = 0
            else:
                pos_second -= 10
        elif command == 'next':
            if video_len_second - pos_second < 10:
                pos_second = video_len_second
            else:
                pos_second += 10

        if op_start_second <= pos_second <= op_end_second:
            pos_second = op_end_second

    minute = str(pos_second // 60)
    second = str(pos_second % 60)

    if len(minute) == 1:
        minute = "0" + minute

    if len(second) == 1:
        second = "0" + second

    answer = minute + ":" + second

    return answer