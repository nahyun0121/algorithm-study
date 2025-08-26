n, m, k = map(int, input().split())  # 공백으로 구분하여 입력받기
data = list(map(int, input().split())) # N개의 수를 공백으로 구분하여 입력받기

# m번 더하여 가장 큰 수
# 연속해서 k번까지만 더할 수 있음

# 내가 생각한 풀이 방법
# 1. 제일 큰 수->작은 수로 정렬, 제일 큰 수 두 개만 가져옴
# 2. 큰 거 꺼내서 k번 더하고 다음 거 꺼내서 1번 더하고, 아직 m번 안 더했다면 다시 이 과정 반복

data.sort()
first = data[n - 1]
second = data[n - 2]

## 1. 단순하게 푸는 방법
# result = 0

# while True:
#     for i in range(k):
#         if m == 0:  # m이 0이라면 반복문 탈출
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second  # 두 번째로 큰 수를 한 번 더하기
#     m -= 1

# print(result)


## 2. 반복되는 수열 고려하여 시간 초과 방지
# 가장 큰 수가 더해지는 횟수 계산
count = m // (k + 1) * k + m % (k + 1)

result = 0
result += first * count + second * (m - count)

print(result)