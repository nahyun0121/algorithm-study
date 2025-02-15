import sys
input = sys.stdin.readline

# 단어를 알파벳 빈도 딕셔너리로 변환
def word_to_freq(word):
    freq = {}
    for char in word:
        freq[char] = freq.get(char, 0) + 1  # dictionary의 get: (찾고자 하는 key, key가 없을 때 리턴할 값)
    return freq

# 퍼즐로 단어를 만들 수 있는지 확인
def can_make_word(puzzle_freq, word_freq):
    return all(word_freq[char] <= puzzle_freq.get(char, 0) for char in word_freq)  # all(): 인자로 넘어온 자료구조 내의 모든 요소가 참일 때만 True 반환

# 가장 적은/많은 단어를 만드는 중앙 글자 찾기
def find_best_worst(puzzle_count):
    sorted_counts = sorted(puzzle_count.items(), key=lambda x: (x[1], x[0]))  # 단어 개수를 기준으로 오름차순 정렬, 같은 개수일 경우 알파벳 순으로 정렬
    min_count, max_count = sorted_counts[0][1], sorted_counts[-1][1]
    min_chars = "".join(char for char, count in sorted_counts if count == min_count)
    max_chars = "".join(char for char, count in sorted_counts if count == max_count)
    print(min_chars, min_count, max_chars, max_count)

# 단어 입력
word_dict = {}
while (word := input().strip()) != "-":
    if word not in word_dict:
        word_dict[word] = word_to_freq(word)

# 퍼즐 입력
while (puzzle := input().strip()) != "#":
    puzzle_freq = word_to_freq(puzzle)
    puzzle_count = {char: 0 for char in puzzle_freq}  # 각 글자가 중앙일 때 만들 수 있는 단어 개수 저장용 딕셔너리 초기화

    for word_freq in word_dict.values():
        if can_make_word(puzzle_freq, word_freq):
            for char in word_freq:
                puzzle_count[char] += 1

    find_best_worst(puzzle_count)