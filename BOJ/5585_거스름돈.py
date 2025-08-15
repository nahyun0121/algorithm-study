price = int(input())
change = 1000 - price

coin_list = [500, 100, 50, 10, 5, 1]

# 가격이 380엔일 때, 620엔 거슬러 받아야 함
# 500 1개, 100 1개, 10 2개
# 620 -> 120 -> 20 -> 0

# 가격이 1엔일 때, 999엔 거슬러 받아야 함
# 500 1개, 100 4개, 50 1개, 10 4개, 5엔 1개, 1엔 4개

count = 0
for coin in coin_list:
    count += change // coin
    change %= coin
    
print(count)