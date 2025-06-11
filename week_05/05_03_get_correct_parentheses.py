from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parenthesis(string):
    stack = []

    for char in string:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            stack.pop()

    if stack:
        return False
    return True


def separate_to_u_v(string):
    queue = deque(string)
    left_parenthesis_cnt, right_parenthesis_cnt = 0, 0
    u, v = "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == "(":
            left_parenthesis_cnt += 1
        elif char == ")":
            right_parenthesis_cnt += 1

        if left_parenthesis_cnt == right_parenthesis_cnt:
            break

    v = ''.join(queue)
    return u, v


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parenthesis(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parenthesis(balanced_parentheses_string)


def reverse_parenthesis(string):
    reverse_string = ""
    for char in string:
        if char == "(":
            reverse_string += ")"
        elif char == ")":
            reverse_string += "("
    return reverse_string


def change_to_correct_parenthesis(balanced_parentheses_string):
    if balanced_parentheses_string == '':
        return ''
    u, v = separate_to_u_v(balanced_parentheses_string)

    if is_correct_parenthesis(u):
        return  u + change_to_correct_parenthesis(v)
    else:
        return "(" + change_to_correct_parenthesis(v) + ")" + reverse_parenthesis(u[1:-1])


print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))