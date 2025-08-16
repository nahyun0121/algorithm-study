# ----------------------------------------
# 첫 번째 풀이: 글자 단위 출력 + count 관리
# ----------------------------------------
word = input()
length = len(word)
count = 0

# 10글자 미만 처리
if length - count < 10:
    print(word)

else: 
    for i in word:
        print(i, end='')
        count += 1
        # 10글자마다 줄바꿈
        if count % 10 == 0:
            print()


# 만약 len = 13인 문자열 '일이삼사오육칠팔구십일이삼'
# 일, count 1
# 십, count = 10


# --------------------------
# 두 번째 풀이: 슬라이싱 활용
# --------------------------

word = input()

for i in range(0, len(word), 10):
    print(word[i:i+10])
