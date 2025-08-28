n = int(input())
plan = input().split()

y, x = 1, 1  # (행, 열)

for cmd in plan:
    if (cmd == 'L'):
        x = max(1, x - 1)
    elif (cmd =='R'):
        x = min(n, x + 1)
    elif (cmd == 'U'):
        y = max(1, y - 1)
    elif (cmd == 'D'):
        y = min(n, y + 1)

print(y, x)