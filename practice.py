# abilities = list(map(int, input().split()))
# total_ability = sum(abilities)
# n = 6
# ans = None
#
# for i in range(n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             select = abilities[i] + abilities[j] + abilities[k]
#             other = total_ability - select
#
#             temp = abs(select-other)
#
#             if ans is None or ans > temp:
#                 ans = temp
#
# print(ans)
