def is_palindrome(string):
    left, right = 0, len(string) - 1

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            # 유사회문 판별
            remove_left = string[left+1:right+1]
            remove_right = string[left:right]

            if remove_left == remove_left[::-1] or remove_right == remove_right[::-1]:
                return 1
            return 2
    return 0


N = int(input())
for _ in range(N):
    string = input().strip()
    print(is_palindrome(string))