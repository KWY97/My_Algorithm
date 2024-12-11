my_str = input()
alphabet_occurrence_array = [-1] * 26

for i in range(len(my_str)):
    if alphabet_occurrence_array[ord(my_str[i]) - ord('a')] == -1:
        alphabet_occurrence_array[ord(my_str[i]) - ord('a')] = i

print(*alphabet_occurrence_array)