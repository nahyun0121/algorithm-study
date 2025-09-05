n = int(input())

count = 0

# hour=3, 60*60 개

# hour가 3이 아니면서 minute에 3이 들어가는 경우는 60개

# hour, minute에 3이 안 들어가면서 second에만 3이 들어가는 경우는 15개
# 3, 13, 23, 33, 43, 53
# 30, 31, 32, 34, 35, 36, 37, 38, 39


# for hour in range(n+1):
#     if '3' in str(hour):
#         count += 60*60
#         continue
#     for minute in range(60):
#         if '3' in str(minute):
#             count += 60
#             continue
#         count += 15

# print(count)


# -------------------------------------------------------------------
# 방법 2)
# 하루는 86,400초여서 연상량이 86,400번으로 작기 때문에 단순 삼중 루프도 가능!
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            if '3' in f"{hour}{minute}{second}":
                count += 1

print(count)