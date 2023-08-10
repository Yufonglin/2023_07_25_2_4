#猜數字遊戲，亂數猜
import random
min = 1
max = 100
trage = random.randint(1,100)

count =0


print("====猜數字遊戲===\n\n")
while True:
    count +=1
    keyin = int(input(f"猜數字的範圍{min}~{max}:"))
    
    if keyin>=min and keyin<=max:
        if keyin ==trage:
            print(f"恭喜你猜對了，答案是{keyin}")
            print(f"你總共猜了：{count}")
            break
        elif keyin >trage:
            print("在小一點")
            max = keyin-1
        elif keyin < trage:
            print("在大一點")
            min = keyin+1
            print(f"你已經猜了{count}次")

    else:
        print("超出範圍")
print("game over")