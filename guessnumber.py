import random
def guess_number():
    number = random.randint(1, 100)
    count = 0
    while count < 10:
        guess = int(input("请猜一个数字："))
        count += 1
        if guess == number:
            print("恭喜你，猜对了！")
            break
        elif guess > number:
            print("太大了！")
        else:
            print("太小了！")
    else:
        print(f"很抱歉，你没有在10次机会内猜中，答案是{number}。")
guess_number()
#2024.4.21
