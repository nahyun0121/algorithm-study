n = int(input())

# 상단
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)

# 하단
for i in range(1, n):
    print("*" * (n - i) + " " * (2 * i) + "*" * (n - i))