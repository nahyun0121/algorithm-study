n, k = map(int, input().split())

# 1. N이 K의 배수가 될 때까지 -1
# 2. N을 K로 나누기

## 단순하게 푸는 방법
# result = 0
# while n >= k:
#     # N이 K로 나누어 떨어지지 않는다면 1씩 빼기
#     while n % k != 0:
#         n -= 1
#         result += 1
#     # K로 나누기
#     n //= k
#     result += 1

# # 마지막으로 남은 수에 대하여 1씩 빼기
# while n > 1:
#     n -= 1
#     result += 1

# print(result)


## N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식
result = 0
while True:
    # N을 K로 나눌 수 있는 '가장 가까운 배수'로 맞추기
    target = (n // k) * k
    # N을 target까지 1씩 빼는 횟수를 더함
    result += (n - target)
    n = target
    # N이 K보다 작아져 더 이상 나눌 수 없을 때 반복 종료
    if n < k:
        break
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)