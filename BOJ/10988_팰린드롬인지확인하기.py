# word = input()
# is_palinedrome = 1

# for i in range(len(word) // 2):
#     if word[i] != word[-(i+1)]:
#         is_palinedrome = 0
#         break

# print(is_palinedrome)

# # level일 때, 0 - 4 / 1 - 3 / 2 - 2
# # noon일 때, 0 -3 / 1 - 2

word = input()
print(1 if word == word[::-1] else 0)