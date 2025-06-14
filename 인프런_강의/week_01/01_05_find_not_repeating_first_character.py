# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.

def find_not_repeating_first_character(string):
    # string에서 알파벳의 빈도수를 찾는다.
    occurrence_array = find_alphabet_occurrence_array(string)

    # 빈도수가 1인 알파벳들 중에서 srting에서 먼저 나오는 알파벳이 무엇인지 찾아본다.
    not_repeating_character_array = []
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord('a')))

    for char in string:
        if char in not_repeating_character_array:
            return char
    return '_'


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a') # 해당 문자를 인덱스로 치환
        alphabet_occurrence_array[arr_index] += 1 # 빈도수 배열의 인덱스로 찾아가서 개수를 추가
    return alphabet_occurrence_array
        
result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 = _ 현재 풀이 값 =", result("aaaaaaaa"))